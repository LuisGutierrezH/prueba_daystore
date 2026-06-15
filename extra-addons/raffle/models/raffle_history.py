# -*- coding: utf-8 -*-

from odoo import models, fields, api, _


class RaffleHistory(models.Model):
    _name = 'raffle.history'
    _description = 'Histórico de Sorteos'
    _order = 'date desc'

    name = fields.Char(
        string='Número de Sorteo',
        required=True,
        copy=False,
        readonly=True,
        default=lambda self: _('Nuevo')
    )

    product_id = fields.Many2one(
        'product.product',
        string='Premio',
        required=True
    )

    winner_id = fields.Many2one(
        'hr.employee',
        string='Ganador',
        required=True
    )

    date = fields.Datetime(
        default=fields.Datetime.now,
        required=True
    )

    # Método para generar un número de sorteo único
    @api.model
    def create(self, vals):
        if vals.get('name', _('Nuevo')) == _('Nuevo'):
            vals['name'] = self.env['ir.sequence'].next_by_code(
                'raffle.history'
            ) or _('Nuevo')

        return super().create(vals)
    
    # Método para abrir el asistente de sorteo desde el historial
    def action_abrir_wizard(self):
        return {
            'name': 'Tómbola de Lunes',
            'type': 'ir.actions.act_window',
            'res_model': 'raffle.wizard',
            'view_mode': 'form',
            'target': 'new',
            'context': {
                'default_product_id': self.product_id.id,
            }
        }
    # Método para abrir el menú de la tómbola desde el historial en la barra del menú   
    def action_menu_lanzar_tombola(self):
        return {
            'name': 'Tómbola Mundialista',
            'type': 'ir.actions.act_window',
            'res_model': 'raffle.wizard',
            'view_mode': 'form',
            'target': 'new',
            'context': {
                'default_product_id': False, 
            }
        }