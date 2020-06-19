
from odoo import models, fields, api, _
from datetime import date

class QbItemsBank(models.Model):
    _name = 'qb.items'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Scheme of Assessment Table'
    _rec_name = 'Item_Description'

    @api.model
    def create(self, vals):
        if vals.get('Item_ID', _('New')) == _('New'):
            vals['Item_ID'] = self.env['ir.sequence'].next_by_code('qb.items.sequence') or _('New')
        result = super(QbItemsBank, self).create(vals)
        return result

    def get_responses_count(self):
        count = self.env['qb.items.responses'].search_count([('Item_ID', '=', self.id)])
        self.No_of_Responses = count

    Item_ID = fields.Char(string='Items Sequence', required=True, copy=False, readonly=True,
                           index=True, default=lambda self: _('New'))
    # Command_Word_ID = fields.Many2one(string="Command Word")
    Item_Description = fields.Text(string="Item Description")
    Is_Item_Image = fields.Binary(string='Item Images', required=False)
    Topic_ID = fields.Many2one('qb.topics', string='Topic', required=False)
    SLO_ID = fields.Many2one('qb.scheme', string='SLO', required=False)
    Item_Type_ID = fields.Many2one('qb.itemtypes', string='Item Type', required=False)
    Question_Weight = fields.Integer(string="Question Weight")
    Version_No = fields.Integer(string="Version No")
    Version_Counts = fields.Integer(string="Version Counts")
    No_of_Responses = fields.Integer(string="No of Responses", compute='get_responses_count')
    Active = fields.Boolean(string="Active")
    # Off_Line = fields.Char(string="Off Line")
    Question_Established_By = fields.Many2one('res.users', string="Established By")
    Question_Established_Date = fields.Date(string="Established Date", default=date.today())
    Approved = fields.Boolean(string="Approved")
    Question_Approved_By = fields.Char(string="Approved By")
    Question_Approved_Date = fields.Date(string="Approved Date")
    Item_Responses = fields.One2many('qb.items.responses', 'Item_ID', string="Item Responses")


    class QbItemsBankResponses(models.Model):
        _name = 'qb.items.responses'
        _description = 'Item Responses'

        # Response_ID = fields.Integer(string="Response ID")
        # Response_No = fields.Char(string="Response No")
        Option_ID = fields.Many2one('qb.options', string='Option')
        Response_Description = fields.Char(string="Response Description")
        Correct = fields.Boolean(string="Correct Option")
        Response_Weight = fields.Integer(string="Response Weight")
        Is_Response_Image = fields.Binary(string='Response Image')
        Item_ID = fields.Many2one('qb.items', string='Item ID')

