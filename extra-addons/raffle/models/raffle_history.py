# -*- coding: utf-8 -*-
import logging

from odoo import models, fields, api, _
# from odoo.exceptions import UserError, ValidationError

_logger = logging.getLogger(__name__)


class RaffleHistory(models.Model):
    _name = 'raffle.history'
    _description = 'Histórico de Sorteos'
    _order = 'date desc'
    name = fields.Char(string='Número de Sorteo', required=True, copy=False, readonly=True, index=True, default=lambda self: _('Nuevo'))

    product_id = fields.Many2one('product.product', string='Premio', required=True,
                                 domain=[('product_tmpl_id.is_souvenir', '=', True)])

    winner_id = fields.Many2one('hr.employee', string='Ganador', required=True)

    date = fields.Datetime(default=fields.Datetime.now, required=True)

@api.model
def create(self, vals):

    if vals.get('name', _('Nuevo')) == _('Nuevo'):
        vals['name'] = self.env['ir.sequence'].next_by_code(
            'raffle.history'
        ) or _('Nuevo')
    return super(RaffleHistory, self).create(vals)
 