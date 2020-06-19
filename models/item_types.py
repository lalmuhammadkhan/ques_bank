
from odoo import models, fields, api, _

class QbItemTypes(models.Model):
    _name = 'qb.itemtypes'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Item Type Table'
    _rec_name = 'Item_Type'

    Item_Type_ID = fields.Char(string='Type Sequence', required=True, copy=False, readonly=True,
                           index=True, default=lambda self: _('New'))
    Item_Type = fields.Char(string="Type Level Name")

    @api.model
    def create(self, vals):
        if vals.get('Item_Type_ID', _('New')) == _('New'):
            vals['Item_Type_ID'] = self.env['ir.sequence'].next_by_code('qb.itemtypes.sequence') or _('New')
        result = super(QbItemTypes, self).create(vals)
        return result
