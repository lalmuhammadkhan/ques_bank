
from odoo import models, fields, api, _
from datetime import date

class QbItemsSubjectives(models.Model):
    _name = 'qb.subjective'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Scheme of Assessment Table'
    _rec_name = 'Item_Description'

    @api.model
    def create(self, vals):
        if vals.get('Item_ID', _('New')) == _('New'):
            vals['Item_ID'] = self.env['ir.sequence'].next_by_code('qb.subjective.sequence') or _('New')
        result = super(QbItemsSubjectives, self).create(vals)
        return result

    @api.onchange('Grade_ID')
    def onchange_Grade_ID(self):
        for rec in self:
            return {'domain': {'Subject_ID': [('Grade_ID', '=', rec.Grade_ID.id)]}}

    @api.onchange('Subject_ID')
    def onchange_Grade_ID(self):
        for rec in self:
            return {'domain': {'Section_ID': [('Subject_ID', '=', rec.Subject_ID.id)]}}

    @api.onchange('Section_ID')
    def onchange_Grade_ID(self):
        for rec in self:
            return {'domain': {'Chapter_Unit_ID': [('Section_ID', '=', rec.Section_ID.id)]}}

    @api.onchange('Chapter_Unit_ID')
    def onchange_Grade_ID(self):
        for rec in self:
            return {'domain': {'Topic_ID': [('Chapter_Unit_ID', '=', rec.Chapter_Unit_ID.id)]}}

    @api.model
    def default_get(self, fields):
        res = super(QbItemsSubjectives, self).default_get(fields)
        print('default get function is calling')
        res['Item_Type_ID'] = 2
        # res['notes'] = 'Default Get to populate the values'
        return res

    Item_ID = fields.Char(string='Items Sequence', required=True, copy=False, readonly=True,
                           index=True, default=lambda self: _('New'))
    # Command_Word_ID = fields.Many2one(string="Command Word")
    Item_Description = fields.Text(string="Item Description")
    Item_Answer = fields.Text(string="Item Answer")
    Is_Item_Image = fields.Binary(string='Item Images', required=False)
    Topic_ID = fields.Many2one('qb.topics', string='Topic', required=False)
    SLO_ID = fields.Many2one('qb.scheme', string='SLO', required=False)
    Item_Type_ID = fields.Many2one('qb.itemtypes', string='Item Type', required=False)
    Question_Weight = fields.Integer(string="Question Weight")
    Version_No = fields.Integer(string="Version No")
    Version_Counts = fields.Integer(string="Version Counts")
    Active = fields.Boolean(string="Active")
    # Off_Line = fields.Char(string="Off Line")
    Question_Established_By = fields.Many2one('res.users', string="Established By")
    Question_Established_Date = fields.Date(string="Established Date", default=date.today())
    Approved = fields.Boolean(string="Approved")
    Question_Approved_By = fields.Many2one('res.users', string="Approved By")
    Question_Approved_Date = fields.Date(string="Approved Date")
    Grade_ID = fields.Many2one('qb.grades', string='Grade')
    Subject_ID = fields.Many2one('qb.subjects', string='Subject')
    Section_ID = fields.Many2one('qb.sections', string='Section')
    Chapter_Unit_ID = fields.Many2one('qb.units', string='Chapter')
