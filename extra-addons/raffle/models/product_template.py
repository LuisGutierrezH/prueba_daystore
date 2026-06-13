# -*- coding: utf-8 -*-
import logging

from odoo import models, fields, api, _
# from odoo.exceptions import UserError, ValidationError

_logger = logging.getLogger(__name__)


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    raffle_coin_value = fields.Integer(string='Monedas necesarias', required=False)
    is_souvenir = fields.Boolean(string='Souvenir', default=False)
