# -*- coding: utf-8 -*-
import logging

from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError

_logger = logging.getLogger(__name__)


class CrmLead(models.Model):
    _inherit = 'crm.lead'


    development_id          = fields.Many2one('crm.developments', 'Desarrollo',tracking=True)
    first_payment           = fields.Boolean('Primer pago',tracking=True)
    quantity_payment        = fields.Selection(selection=[('1','1'),('2','2'),('3','3'),('4','4'),('5','5')],string='Cantidad de pagos',tracking=True)
    honorarium              = fields.Monetary('Propuesta de honorarios 1',currency_field="company_currency", required=False, default=0.0, tracking=True)
    honorarium_two_proposal = fields.Monetary('Propuesta de honorarios 2',currency_field="company_currency", required=False, default=0.0, tracking=True)
    one_payment             = fields.Monetary('Primer pago',currency_field="company_currency", required=False, default=0.0, tracking=True)
    second_payment          = fields.Monetary('Segundo pago',currency_field="company_currency", required=False, default=0.0, tracking=True)
    three_payment           = fields.Monetary('Tercer pago',currency_field="company_currency", required=False, default=0.0, tracking=True)
    three_payment_date       = fields.Date(string="Fecha tercer pago",tracking=True)
    four_payment           = fields.Monetary('Cuarto pago',currency_field="company_currency", required=False, default=0.0, tracking=True)
    four_payment_date       = fields.Date(string="Fecha cuarto pago",tracking=True)
    five_payment           = fields.Monetary('Quinto pago',currency_field="company_currency", required=False, default=0.0, tracking=True)
    five_payment_date       = fields.Date(string="Fecha quinto pago",tracking=True)
    number_to_words         = fields.Char(string="Monto en letras (Total) :",compute='_compute_number_to_words')
    currency_id             = fields.Many2one('res.currency', string='Moneda',tracking=True)
    new_development         = fields.Char(string="Desarrollo", tracking=True)
    matter                  = fields.Selection([
        ('in_five_days', 'Estoy dentro de los 5 días hábiles '),('sign_five_afer', 'Firmé hace más de 5 días hábiles'), 
        ('other', 'Otro')], 'Asunto', tracking=True)


    @api.onchange('quantity_payment')
    def onchange_quantity_payment(self):

        self.one_payment = 0
        self.second_payment = 0
        self.three_payment = 0
        self.four_payment = 0
        self.five_payment = 0
        self.three_payment_date = False
        self.four_payment_date = False
        self.five_payment_date = False

    def _compute_number_to_words(self):
        """Compute the amount to words in Sale Order"""
        for rec in self:
            if rec.honorarium_two_proposal > 0:
                rec.number_to_words = rec.company_currency.amount_to_text(
                    rec.honorarium_two_proposal)
            else:
                rec.number_to_words = rec.company_currency.amount_to_text(
                    rec.honorarium)


    def auto_asignation(self):

        logging.info("\033[32m {}\033[00m" .format("Auto asignacion"))

        self.env['crm.lead'].search([])
        teams = self.env['crm.team'].search([])

        current_value = 0
        team_to_assign = 0

        for team in teams:
            leads_by_team = self.env['crm.lead'].search([('team_id.id','=',team.id)])
            if current_value < len(leads_by_team):
                current_value = len(leads_by_team)
            
        logging.info("\033[32m {}\033[00m" .format(team_to_assign))
               
        self.team_id.id = team_to_assign
