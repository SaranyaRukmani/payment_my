# -*- coding: utf-8 -*-

from odoo import models, fields, api

class payment_my(models.Model):
     _name = 'payment_my.payment_my'

     ac_id = fields.Integer()
     is_active = fields.Boolean(string='Active', default=True)
     create_date = fields.Date(string="Date")
     description = fields.Char()
#	 acty=f.man

#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100
class card_provider(models.Model):
     _name = 'payment_my.card_provider'

     id = fields.Integer()
     code = fields.Integer()
     description = fields.Char()