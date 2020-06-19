
from odoo import models, fields, api, _

class QbSubjects(models.Model):
    _name = 'qb.subjects'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Subjects Table'
    _rec_name = 'Subject_Name'

    Subject_ID = fields.Char(string='Subject Sequence', required=True, copy=False, readonly=True,
                           index=True, default=lambda self: _('New'))
    Subject_Name = fields.Char(string="Subject Name")
    Session = fields.Text(string="Session")
    Grade_ID = fields.Many2one('qb.grades', string='Grade', required=False)

    @api.model
    def create(self, vals):
        if vals.get('Subject_ID', _('New')) == _('New'):
            vals['Subject_ID'] = self.env['ir.sequence'].next_by_code('qb.subjects.sequence') or _('New')
        result = super(QbSubjects, self).create(vals)
        return result
