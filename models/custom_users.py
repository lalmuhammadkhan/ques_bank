from odoo import models, fields, api, _
from ast import literal_eval


class groups(models.Model):
    _inherit = 'res.groups'

    note = fields.Char(string='Default Note')
    Subject_ID = fields.Many2many('qb.subjects', string="Subjects")

    # def set_values(self):
    #     res = super(QCustomUsers, self).set_values()
    #     self.env['ir.config_parameter'].sudo().set_param('ques_bank.note', self.note)
    #     self.env['ir.config_parameter'].sudo().set_param('ques_bank.Subject_ID', self.Subject_ID.ids)
    #     return res
    #
    # @api.model
    # def get_values(self):
    #     res = super(QCustomUsers, self).get_values()
    #     # ICPSudo = self.env['ir.config_parameter'].sudo()
    #     # notes = ICPSudo.get_param('om_hospital.note')
    #     note = self.env['ir.config_parameter'].sudo().get_param('ques_bank.note')
    #     Subject_ID = self.env['ir.config_parameter'].sudo().get_param('ques_bank.Subject_ID')
    #     res.update(
    #         note=note,
    #         Subject_ID=[(6, 0, literal_eval(Subject_ID))] if Subject_ID else False,
    #     )
    #     return res