from collections import defaultdict
from odoo import api, models, fields, _
from datetime import datetime



class trasnfersData(models.Model):
    _name = 'transfers.data'
    _rec_name = 'number_seq'

    @api.depends()
    def get_gold_count(self):
        for record in self:
            record.gold_count = self.env['transfers.data'].search_count(
                [('id', '=', self.id)])


    owner = fields.Many2one('res.partner', required= True)
    date = fields.Date(default= datetime.today(), required = True)
    date_of_sale = fields.Date()
    sale_price = fields.Integer()
    transaction_type = fields.Selection(
        string='Transaction_type',
        selection=[('cash', 'Cash'),
                   ('cheque', 'Cheque'), ],
        required=False, )

    specimen_weight = fields.Float()
    weight = fields.Float()
    calibre = fields.Integer(required =True)
    net_weight = fields.Float(compute = "get_net_weight", readonly  = True)
    number_seq = fields.Text()




    @api.model
    def create(self, vals):
        if vals.get('number_seq', _('New')) == _('New'):
            vals['number_seq'] = self.env['ir.sequence'].next_by_code('transfer.sequence') or _('New')
        delta = super(trasnfersData, self).create(vals)
        return delta
    @api.depends('weight','calibre','specimen_weight')
    def get_net_weight(self):
        for rec in self:
            rec.net_weight = (rec.weight + rec.specimen_weight) / 875 * rec.calibre


class contactInherit(models.Model):
    _inherit = ['res.partner']

    gold_count = fields.Integer(compute=trasnfersData.get_gold_count())
    namen = fields.Char()

