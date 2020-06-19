
from odoo import models, fields, api, _

class QbSections(models.Model):
    _name = 'qb.sections'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Section Table'
    _rec_name = 'Section_Name'

    Section_ID = fields.Char(string='Section Sequence', required=True, copy=False, readonly=True,
                           index=True, default=lambda self: _('New'))
    Section_Name = fields.Char(string="Section Name")
    Weightage = fields.Integer(string="Weightage")
    Subject_ID = fields.Many2one('qb.subjects', string='Subjects', required=False)

    @api.model
    def create(self, vals):
        if vals.get('Section_ID', _('New')) == _('New'):
            vals['Section_ID'] = self.env['ir.sequence'].next_by_code('qb.Sections.sequence') or _('New')
        result = super(QbSections, self).create(vals)
        return result
