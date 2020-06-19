from odoo import models, fields, api, _
from ast import literal_eval


class QBankSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    note = fields.Char(string='Default Note')
    module_crm = fields.Boolean(string="CRM")
    Subject_ID = fields.Many2many('qb.subjects', string="Subjects")

    def set_values(self):
        res = super(QBankSettings, self).set_values()
        self.env['ir.config_parameter'].sudo().set_param('ques_bank.note', self.note)
        self.env['ir.config_parameter'].sudo().set_param('ques_bank.Subject_ID', self.Subject_ID.ids)
        return res

    @api.model
    def get_values(self):
        res = super(QBankSettings, self).get_values()
        # ICPSudo = self.env['ir.config_parameter'].sudo()
        # notes = ICPSudo.get_param('om_hospital.note')
        note = self.env['ir.config_parameter'].sudo().get_param('ques_bank.note')
        Subject_ID = self.env['ir.config_parameter'].sudo().get_param('ques_bank.Subject_ID')
        res.update(
            note=note,
            Subject_ID=[(6, 0, literal_eval(Subject_ID))] if Subject_ID else False,
        )
        return res