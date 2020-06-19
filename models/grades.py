
from odoo import models, fields, api, _

class QbGrades(models.Model):
    _name = 'qb.grades'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Grades Table'
    _rec_name = 'Description'

    Grade_ID = fields.Char(string='Grade Sequence', required=True, copy=False, readonly=True,
                           index=True, default=lambda self: _('New'))
    Grade_Name = fields.Char(string="Grade Name")
    Description = fields.Text(string="Grade Description")

    @api.model
    def create(self, vals):
        if vals.get('Grade_ID', _('New')) == _('New'):
            vals['Grade_ID'] = self.env['ir.sequence'].next_by_code('qb.grades.sequence') or _('New')
        result = super(QbGrades, self).create(vals)
        return result
