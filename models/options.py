
from odoo import models, fields, api, _

class QbOptions(models.Model):
    _name = 'qb.options'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Options Table'
    _rec_name = 'Option_Name'

    Option_ID = fields.Char(string='Option Sequence', required=True, copy=False, readonly=True,
                           index=True, default=lambda self: _('New'))
    Option_Name = fields.Char(string="Option Name")

    @api.model
    def create(self, vals):
        if vals.get('Option_ID', _('New')) == _('New'):
            vals['Option_ID'] = self.env['ir.sequence'].next_by_code('qb.options.sequence') or _('New')
        result = super(QbOptions, self).create(vals)
        return result
