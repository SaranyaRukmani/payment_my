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
class cardtype(models.Model):
	_name = 'payment_my.cardtype'

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
	IsActive = fields.Boolean(string="Active",default=True)
	CreatedDate = fields.Date(String="Date")
	

class ContractType(models.Model):
	_name = 'payment_my.contract_type'

	Id = fields.Integer()
	Code = fields.Integer()
	Description = fields.Char()
	
class Country(models.Model):
	_name = 'payment_my.country'

	Id = fields.Integer()
	Code = fields.Integer()
	Country = fields.Char()

class Category(models.Model):
	_name = 'payment_my.category'

	id = fields.Integer()
	code = fields.Integer()
	description = fields.Char()
	
	invoice_ids=fields.One2many('payment_my.invoice', 'category_id', string="Invoice")

class Customer(models.Model):
	_inherit = 'res.partner' 

	first_name = fields.Char(string="First Name")
	middle_name = fields.Char(string="Middle Name")
	last_name = fields.Char(string="Last Name")
	dob = fields.Date(string="Date of birth")
	is_active = fields.Boolean(string='Active', default=True)
	create_date = fields.Date(string="Create Date")
	customer_id = fields.Char(string="ID")
#	cou_id=one2many(country)

class CustomerBankAccount(models.Model):
	_name = 'payment_my.customerbankaccount'

	id = fields.Integer()	
	customer_id = fields.Integer()
	bank_account_id = fields.Integer()

class CreditCard(models.Model):
	_name = 'payment_my.credit_card'

	card_id = fields.Integer(string="ID")
	customer_id = fields.Integer()
	name_on_card = fields.Char()
	card_no = fields.Integer()
	expiry_date = fields.Date()
	Issue_date = fields.Date()
	card_type_id =fields.Integer()
	card_provider_id = fields.Integer()
	is_active = fields.Boolean(string="Active",default=True)
	create_date = fields.Date()
	
class CustomerDevice(models.Model):
	_name = 'payment_my.customer_device'

	Id = fields.Integer()
	CustomerId = fields.Integer()
	DeviceId = fields.Integer()
	MobileNumber= fields.Integer()
	PaymentTypeId = fields.Integer()
	IsActive = fields.Boolean(string="Active",default=True)
	CreatedDate = fields.Date(String="Date")
#	customer_id=one2many(customer_device)
	device_id=fields.Many2one('payment_my.device', string="Device")
	payment_id=fields.Many2one('payment_my.device_payment_type', string="DevicePaymentType")

class Device(models.Model):
	_name = 'payment_my.device'

	Id = fields.Integer()
	DeviceCode = fields.Integer()
	PlatformTypeId = fields.Integer()
	PlatformVersion= fields.Integer()
	IsCameraEnabled = fields.Boolean(string="Active",default=True)
	IsCameraCanReadQRCode = fields.Boolean(string="Active",default=True)
	IsNFCOpen = fields.Boolean(string="Active",default=True)
	AppVersion = fields.Char()
	ApiKey = fields.Integer()
	ApiSecret = fields.Integer()
	CreatedDate = fields.Date(String="Date")
	HashCode = fields.Integer()
	
	customer_device_ids = fields.One2many('payment_my.customer_device', 'device_id', string="customer_device")
	
class DevicePaymentType(models.Model):
	_name = 'payment_my.device_payment_type'

	Id = fields.Integer()
	Code = fields.Integer()
	Description = fields.Char()
	device_payment_type_ids = fields.One2many('payment_my.customer_device', 'payment_id', string="customer_device")
	
class DevicePlatform(models.Model):
	_name = 'payment_my.device_platform'

	Id = fields.Integer()
	Code = fields.Integer()
	Description = fields.Char()
	
class EventType(models.Model):
	_name = 'payment_my.even_type'

	Id = fields.Integer()
	Code = fields.Integer()
	Description = fields.Char()
	
	
class Invoice(models.Model):
	_name = 'payment_my.invoice'

	Id = fields.Integer()
	InvoiceCode = fields.Integer()
	MerchantId = fields.Integer()
	CategoryId= fields.Integer()
	MerchantInvoiceReference = fields.Char()
	Amount = fields.Integer()
	CreatedBy = fields.Char()
	MerchantDeviceId = fields.Integer()
	CreatedDate = fields.Date(String="Date")
	ExpiryDate = fields.Date(String="Date")
	CustomerId = fields.Integer()
	Description = fields.Char()
	StatusId = fields.Integer()
	CreatedDateStamp = fields.Date(String="Date")
	
	category_id=fields.Many2one('payment_my.category', string="Category")

class InvoiceStatus(models.Model):
	_name = 'payment_my.invoice_status'

	Id = fields.Integer()
	Code = fields.Integer()
	Description = fields.Char()
