from odoo import models, fields, api, _


class partnerDetails(models.Model):
    _name = 'partner.details'
    _description = 'A new partner'
    _rec_name = 'partner_name'
    _order = 'partner_name asc'

    partner_name = fields.Many2one('res.partner', required=True, string='Name')
    phone_number = fields.Char()
    bars_count = fields.Integer(compute='get_bars_count')
    sold_bars_count = fields.Integer(compute='get_sold_bars_count')


    def smart_button_gold_object(self):
        return {
            'name': _("Gold Bars"),
            'domain': [('owner', '=', self.id)],
            'type': 'ir.actions.act_window',
            'res_model': 'transfers.data',
            'view_mode': 'tree,form',
            'view_type': 'form',
            'view_id': False,
            'context': {'create': False},
        }

    def smart_button_gold_object_sold(self):
        return {
            'name': _("Gold Bars"),
            'domain': [('owner', '=', self.id),('bar_state', '=', 'yes')],
            'type': 'ir.actions.act_window',
            'res_model': 'transfers.data',
            'view_mode': 'tree,form',
            'view_type': 'form',
            'view_id': False,
            'context': {'create': False},
        }

    def get_bars_count(self):
        self.bars_count = self.env['transfers.data'].search_count([('owner', '=', self.id)])

    def get_sold_bars_count(self):
        self.sold_bars_count = self.env['transfers.data'].search_count([('owner', '=', self.id), (
        'bar_state', '=', 'yes')])