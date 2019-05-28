# -*- coding: utf-8 -*-
from odoo import http

# class PaymentMy(http.Controller):
#     @http.route('/payment_my/payment_my/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/payment_my/payment_my/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('payment_my.listing', {
#             'root': '/payment_my/payment_my',
#             'objects': http.request.env['payment_my.payment_my'].search([]),
#         })

#     @http.route('/payment_my/payment_my/objects/<model("payment_my.payment_my"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('payment_my.object', {
#             'object': obj
#         })