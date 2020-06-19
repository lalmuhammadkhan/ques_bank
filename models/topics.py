
from odoo import models, fields, api, _

class QbTopics(models.Model):
    _name = 'qb.topics'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Topics Table'
    _rec_name = 'Topic_Name'

    Topic_ID = fields.Char(string='Topic Sequence', required=True, copy=False, readonly=True,
                           index=True, default=lambda self: _('New'))
    Topic_Name = fields.Char(string="Topic Name")
    Chapter_Unit_ID = fields.Many2one('qb.units', string='Chapter', required=False)

    @api.model
    def create(self, vals):
        if vals.get('Topic_ID', _('New')) == _('New'):
            vals['Topic_ID'] = self.env['ir.sequence'].next_by_code('qb.topics.sequence') or _('New')
        result = super(QbTopics, self).create(vals)
        return result
