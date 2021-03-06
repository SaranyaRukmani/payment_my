# -*- coding: utf-8 -*-
{
    'name': "Payment_my",

    'summary': """
        demo project""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/credit_card.xml',
        'views/customer.xml',
        'views/category.xml',
        'views/card_provider.xml',
        'views/account_type_view.xml',
        'views/bank_views.xml',
		'views/bank_account_view.xml',
		'views/contract_type_view.xml',

		'views/customer_bank_account.xml',

		'views/customer_device_view.xml',

		'views/cardtype.xml',

		'views/customereventtransaction.xml',
		'views/device_view.xml',
		'views/device_payment_type_view.xml',
		'views/device_platform_view.xml',
		'views/even_type_view.xml',
		'views/invoice_view.xml',
		'views/invoice_status_view.xml',
		'views/merchant_even_transaction_view.xml',

        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}