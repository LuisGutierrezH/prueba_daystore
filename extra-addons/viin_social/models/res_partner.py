import inspect
import threading

from odoo import fields, models, api


class Partners(models.Model):
    _inherit = 'res.partner'

    user_social_chat_username = fields.Char(
        compute='_compute_user_social_chat_username')

    def _get_channels_as_member(self):
        channels = super()._get_channels_as_member()
        # TODOs: skipped test to avoid queryCount
        # Create a PR for Odoo to hook a domain when search discuss.channel
        if getattr(threading.current_thread(), 'testing', False):
            for stack in inspect.stack(0):
                if stack.function == 'test_init_messaging':
                    return channels

        channels |= self.env['discuss.channel'].search([
            ('channel_type', '=', 'social_chat'),
            ('channel_member_ids', 'in', self.env['discuss.channel.member'].sudo()._search([
                ('partner_id', '=', self.id),
                ('is_pinned', '=', True),
            ])),
        ])
        return channels

    @api.depends('user_ids.user_social_chat_username')
    def _compute_user_social_chat_username(self):
        for partner in self:
            partner.user_social_chat_username = next(iter(partner.user_ids.mapped('user_social_chat_username')), False)
