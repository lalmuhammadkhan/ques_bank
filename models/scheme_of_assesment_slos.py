
from odoo import models, fields, api, _

class QbSchemeofAssesment(models.Model):
    _name = 'qb.scheme'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Scheme of Assessment Table'
    _rec_name = 'SLO_Description'

    SLO_ID = fields.Char(string='SLO Sequence', required=True, copy=False, readonly=True,
                           index=True, default=lambda self: _('New'))
    SLO_Description = fields.Char(string="SLOs Description")
    Topic_ID = fields.Many2one('qb.topics', string='Topic', required=False)
    Cognitive_Level_ID = fields.Many2one('qb.cognitive', string='Cognitive Level', required=False)

    @api.model
    def create(self, vals):
        if vals.get('SLO_ID', _('New')) == _('New'):
            vals['SLO_ID'] = self.env['ir.sequence'].next_by_code('qb.scheme.sequence') or _('New')
        result = super(QbSchemeofAssesment, self).create(vals)
        return result
