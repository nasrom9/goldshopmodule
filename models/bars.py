from collections import defaultdict
from odoo import api, models, fields, _
from datetime import datetime


class barsData(models.Model):
    _name = 'transfers.data'
    _rec_name = 'number_seq'
    _inherit = ["mail.activity.mixin", "mail.thread"]

    bar_state = fields.Selection(
        selection=[('yes', 'Sold'),
                   ('no', 'New'),('invoiced', 'Invoiced')],
        default='no')

    owner = fields.Many2one('partner.details', required=True)
    date = fields.Date(default=datetime.today(), required=True)
    date_of_sale = fields.Date()
    sale_price = fields.Integer()
    transaction_type = fields.Selection(
        string='Transaction_type',
        selection=[('cash', 'Cash'),
                   ('cheque', 'Cheque'), ],
        required=False, )

    specimen_weight = fields.Float()
    weight = fields.Float()
    calibre = fields.Integer(required=True)
    net_weight = fields.Float(compute="get_net_weight", readonly=True)
    number_seq = fields.Text(string="#")

    @api.model
    def create(self, vals):
        if vals.get('number_seq', _('New')) == _('New'):
            vals['number_seq'] = self.env['ir.sequence'].next_by_code('transfer.sequence') or _('New')
        delta = super(barsData, self).create(vals)
        return delta

    @api.depends('weight', 'calibre', 'specimen_weight')
    def get_net_weight(self):
        for rec in self:
            rec.net_weight = (rec.weight + rec.specimen_weight) / 875 * rec.calibre

    # this function will be called every day at 12am to reset the sequence
    # other things to consider: 00
    # what if we want to add a bar from a date that is a bit old?
    # how the sequence should look like?
    def restart_sequence(self):
        sequence = self.env['ir.sequence'].search([('name', '=like', 'transfers.sequence')])
        sequence.write({'number_next_actual': 1})

    def bar_sold(self):
        self.bar_state = 'yes'

    def bar_new(self):
        self.bar_state = 'no'

    def bar_invoiced(self):
        self.bar_state = 'invoiced'
