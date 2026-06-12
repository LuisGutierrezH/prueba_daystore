# -*- coding: utf-8 -*-
import logging

from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError

_logger = logging.getLogger(__name__)


class CrmDevelopments(models.Model):
    _name = 'crm.developments'
    _description = 'Desarrollo'

    name = fields.Char('Nombre')
    description = fields.Char('Descripción')
