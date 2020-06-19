
from odoo import models, fields, api, _

class QbCognitiveLevel(models.Model):
    _name = 'qb.cognitive'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Cognitive Table'
    _rec_name = 'Cognitive_Level_Name'

    Cognitive_Level_ID = fields.Char(string='Cognitive Sequence', required=True, copy=False, readonly=True,
                           index=True, default=lambda self: _('New'))
    Cognitive_Level_Name = fields.Char(string="Cognitive Level Name")
    Cognitive_Priority = fields.Integer(string='Cognitive Priority')

    @api.model
    def create(self, vals):
        if vals.get('Cognitive_Level_ID', _('New')) == _('New'):
            vals['Cognitive_Level_ID'] = self.env['ir.sequence'].next_by_code('qb.cognitive.sequence') or _('New')
        result = super(QbCognitiveLevel, self).create(vals)
        return result
