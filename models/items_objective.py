
from odoo import models, fields, api, _
from datetime import date

class QbItemsObjectives(models.Model):
    _name = 'qb.objective'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Scheme of Assessment Table'
    _rec_name = 'Item_Description'

    @api.model
    def create(self, vals):
        if vals.get('Item_ID', _('New')) == _('New'):
            vals['Item_ID'] = self.env['ir.sequence'].next_by_code('qb.objective.sequence') or _('New')
        result = super(QbItemsObjectives, self).create(vals)
        return result

    def get_responses_count(self):
        count = self.env['qb.objective.responses'].search_count([('Item_ID', '=', self.id)])
        self.No_of_Responses = count
    #
    # def _get_default_note(self):
    #     return 2

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
        res = super(QbItemsObjectives, self).default_get(fields)
        print('default get function is calling')
        res['Item_Type_ID'] = 1
        # res['notes'] = 'Default Get to populate the values'
        return res

    Item_ID = fields.Char(string='Items Sequence', required=True, copy=False, readonly=True,
                           index=True, default=lambda self: _('New'))
    # Command_Word_ID = fields.Many2one(string="Command Word")
    Item_Description = fields.Text(string="Item Description")
    Is_Item_Image = fields.Binary(string='Item Images', required=False)
    Topic_ID = fields.Many2one('qb.topics', string='Topic', required=False)
    SLO_ID = fields.Many2one('qb.scheme', string='SLO', required=False)
    Item_Type_ID = fields.Many2one('qb.itemtypes', string='Item Type')
    Question_Weight = fields.Integer(string="Question Weight")
    Version_No = fields.Integer(string="Version No")
    Version_Counts = fields.Integer(string="Version Counts")
    No_of_Responses = fields.Integer(string="No of Responses", compute='get_responses_count')
    Active = fields.Boolean(string="Active")
    # Off_Line = fields.Char(string="Off Line")
    Question_Established_By = fields.Many2one('res.users', string="Established By", default=lambda self: self.env.user)
    Question_Established_Date = fields.Date(string="Established Date", default=date.today())
    Approved = fields.Boolean(string="Approved")
    Question_Approved_By = fields.Many2one('res.users', string="Approved By", default=lambda self: self.env.user)
    Question_Approved_Date = fields.Date(string="Approved Date")
    Item_Responses = fields.One2many('qb.objective.responses', 'Item_ID', string="Item Responses")
    Grade_ID = fields.Many2one('qb.grades', string='Grade')
    Subject_ID = fields.Many2one('qb.subjects', string='Subject')
    Section_ID = fields.Many2one('qb.sections', string='Section')
    Chapter_Unit_ID = fields.Many2one('qb.units', string='Chapter')


    class QbItemsBankResponses(models.Model):
        _name = 'qb.objective.responses'
        _description = 'Item Responses'

        # Response_ID = fields.Integer(string="Response ID")
        # Response_No = fields.Char(string="Response No")
        Option_ID = fields.Many2one('qb.options', string='Option')
        Response_Description = fields.Char(string="Response Description")
        Correct = fields.Boolean(string="Correct Option")
        Response_Weight = fields.Integer(string="Response Weight")
        Is_Response_Image = fields.Binary(string='Response Image')
        Item_ID = fields.Many2one('qb.objective', string='Item ID')

