from collections import defaultdict
from odoo import api, models, fields, _
from datetime import datetime

class trasnfersData(models.Model):
    _name = 'transfers_data'
    _rec_name = 'number_seq'
    _order = ""

    date = fields.Date(default= datetime.today, required = True)
    specimen_weight = fields.Float()
    weight = fields.Float()
    calibre = fields.Integer()
    net_weight = fields.Float(compute = "get_net_weight", readonly  = True)
    number_seq = fields.Text()


    @api.model
    def create(self, vals):
        if vals.get('number_seq', _('New')) == _('New'):
            vals['number_seq'] = self.env['ir.sequence'].next_by_code('transfer.sequence') or _('New')
        delta = super(trasnfersData, self).create(vals)
        return delta
