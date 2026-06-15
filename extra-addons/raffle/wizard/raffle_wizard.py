import random

from odoo import api, fields, models, _
from odoo.exceptions import UserError


class RaffleWizard(models.TransientModel):
    _name = 'raffle.wizard'
    _description = 'Tómbola de Lunes'

    employee_ids = fields.Many2many(
        'hr.employee',
        string='Participantes',
        readonly=True,
    )

    product_id = fields.Many2one(
        'product.product',
        string='Premio',
        domain=[('is_souvenir', '=', True)],
        required=True,
    )

    winner_id = fields.Many2one(
        'hr.employee',
        string='Ganador',
        readonly=True,
    )
    
    
    @api.onchange('product_id')
    def _onchange_product_id(self):
        self.employee_ids = [(5, 0, 0)]

        if not self.product_id:
            return

        employees = self.env['hr.employee'].search([
            ('coins', '>=', self.product_id.raffle_coin_value),
            ('coins', '>=', 40)
        ])

        self.employee_ids = [(6, 0, employees.ids)]

    # Función para realizar el sorteo
    def action_spin(self):
        self.ensure_one()
        participants = self.env['hr.employee'].search([
            ('coins', '>=', self.product_id.raffle_coin_value),
            ('coins', '>=', 40)
        ])
        
        if not participants:
            raise UserError(_('No existen empleados con suficientes monedas para este premio.'))

        if not self.product_id:
            raise UserError(_('Seleccione un premio.'))

        winner = random.choice(participants)
        self.winner_id = winner.id

        self._deduct_stock()

        self.env['raffle.history'].create({
            'winner_id': winner.id,
            'product_id': self.product_id.id,
        })

        all_employees = self.env['hr.employee'].search([])
        all_employees.write({'coins': 0})

        return {
            'type': 'ir.actions.client',
            'tag': 'display_notification',
            'params': {
                'title': _('Sorteo realizado'),
                'message': _('Ganador: %s') % winner.name,
                'type': 'success',
                'sticky': False,
            }
        }

    # 🔹 Descontar stock
    def _deduct_stock(self):
        self.ensure_one()

        product = self.product_id

        if product.qty_available < 1:
            raise UserError(_('No hay stock suficiente.'))

        stock_location = self.env.ref('stock.stock_location_stock')
        customer_location = self.env.ref('stock.stock_location_customers')

        warehouse = self.env['stock.warehouse'].search([], limit=1)

        picking_type = warehouse.out_type_id

        if not picking_type:
            raise UserError(_('No se encontró tipo de picking de salida.'))

        picking = self.env['stock.picking'].create({
            'picking_type_id': picking_type.id,
            'location_id': stock_location.id,
            'location_dest_id': customer_location.id,
        })

        move = self.env['stock.move'].create({
            'name': product.display_name,
            'product_id': product.id,
            'product_uom_qty': 1,
            'product_uom': product.uom_id.id,
            'picking_id': picking.id,
            'location_id': stock_location.id,
            'location_dest_id': customer_location.id,
        })

        move._action_confirm()
        move._action_assign()

        for line in move.move_line_ids:
            line.quantity = 1

        picking.button_validate()