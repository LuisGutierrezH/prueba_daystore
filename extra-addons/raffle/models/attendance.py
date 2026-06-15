# -*- coding: utf-8 -*-
import logging

from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError

_logger = logging.getLogger(__name__)


class Attendance(models.Model):
    _inherit = 'hr.attendance'

    points_awarded = fields.Boolean(default=False)

    def _given_coins(self, amount=10):
        # Dar monedas por registro de asistencia.
        for attendance in self:
            if attendance.employee_id:
                attendance.employee_id.coins += amount

    def create(self, vals):
        attendance = super().create(vals)
        attendance._given_coins(10)
        return attendance


    def write(self, vals):
        res = super().write(vals)

        for attendance in self:
            if (
                'check_out' in vals
                and attendance.check_out
                and not attendance.points_awarded
            ):
                attendance._given_coins(10)
                attendance.points_awarded = True

        return res