# -*- coding: utf-8 -*-
# ©  2015 2011,2013 Michael Telahun Makonnen <mmakonnen@gmail.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

{
    'name': 'Contracts - Initial Settings',
    'version': '1.0',
    'category': 'Generic Modules/Human Resources',
    'author': "Michael Telahun Makonnen <mmakonnen@gmail.com>, Odoo Community Association (OCA)",
    'website': 'http://miketelahun.wordpress.com',
    'license': 'AGPL-3',
    'depends': [
        'hr',
        'hr_contract',
        'hr_job_categories',
        'hr_payroll',
        'hr_security',
        'hr_simplify',
    ],
    'data': [
        'security/ir.model.access.csv',
        'hr_contract_init_workflow.xml',
        'hr_contract_view.xml',
    ],
    'installable': True,
}
