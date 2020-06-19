
from odoo import models, fields, api, _

class QbUnits(models.Model):
    _name = 'qb.units'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Units Table'
    _rec_name = 'Chapter_Unit_Name'

    Chapter_Unit_ID = fields.Char(string='Chapter Sequence', required=True, copy=False, readonly=True,
                           index=True, default=lambda self: _('New'))
    Chapter_Unit_Name = fields.Char(string="Chapter Name")
    Item_Weightage = fields.Integer(string="Item Weightage")
    Section_ID = fields.Many2one('qb.sections', string='Section', required=False)
    # testUser = fields.Many2one('res.users', string="Record Rules User Check")

    @api.model
    def create(self, vals):
        if vals.get('Chapter_Unit_ID', _('New')) == _('New'):
            vals['Chapter_Unit_ID'] = self.env['ir.sequence'].next_by_code('qb.units.sequence') or _('New')
        result = super(QbUnits, self).create(vals)
        return result
