# -*- coding: utf-8 -*-
import logging

from odoo import models, fields, api, _
#from odoo.exceptions import UserError, ValidationError

_logger = logging.getLogger(__name__)


class Employee(models.Model):

    _inherit = ["hr.employee"]
    
    # Campo para almacenar las monedas de cada empleado
    coins = fields.Integer(string="Monedas", readonly=True)