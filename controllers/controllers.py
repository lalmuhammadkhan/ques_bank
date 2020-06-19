# -*- coding: utf-8 -*-
# from odoo import http


# class QuesBank(http.Controller):
#     @http.route('/ques_bank/ques_bank/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/ques_bank/ques_bank/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('ques_bank.listing', {
#             'root': '/ques_bank/ques_bank',
#             'objects': http.request.env['ques_bank.ques_bank'].search([]),
#         })

#     @http.route('/ques_bank/ques_bank/objects/<model("ques_bank.ques_bank"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('ques_bank.object', {
#             'object': obj
#         })
