# -*- coding: utf-8 -*-

from odoo import models, fields, api
import datetime

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


class AccountType(models.Model):
	_name = 'payment_my.account_type'

	Id = fields.Integer()
	Code = fields.Integer()
	Description = fields.Char()
	
class payment_my(models.Model):
	_name = 'payment_my.bank'

	id = fields.Integer()	
	code = fields.Integer()
	description = fields.Char()
	
class Bankaccount(models.Model):
	_name = 'payment_my.bank_account'

	Id = fields.Integer()
	AccountName = fields.Char()
	AccountNumber = fields.Integer()
	BankShortCode= fields.Integer()
	IBANCode = fields.Integer()
	BankId = fields.Integer()
	AuthorizationCode = fields.Integer()
	IsActive = fields.Integer()
	CreatedDate = fields.Date(String="Date")
	

class ContractType(models.Model):
	_name = 'payment_my.contract_type'

	Id = fields.Integer()
	Code = fields.Integer()
	Description = fields.Char()

