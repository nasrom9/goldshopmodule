from odoo import models, fields, api, _


class partnerDetails(models.Model):
    _name = 'partner.details'
    _description = 'A new partner'
    _rec_name = 'partner_name'
    _order = 'partner_name asc'

    partner_name = fields.Many2one('res.partner', required=True, string='Name')
    phone_number = fields.Char()

