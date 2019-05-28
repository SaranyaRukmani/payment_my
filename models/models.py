# -*- coding: utf-8 -*-

from odoo import models, fields, api

class payment_my(models.Model):
     _name = 'payment_my.payment_my'

     id = fields.Integer()
     is_active = fields.Integer()
     create_date = fields.Integer()
     description = fields.Char()
#	 acty=f.man

#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100