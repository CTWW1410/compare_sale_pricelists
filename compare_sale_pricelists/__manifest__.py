# -*- coding: utf-8 -*-
##############################################################################
# Odoo Additional Function by CTWW
##############################################################################
{
    'name': "Compare Sale Pricelists",

    'summary': """Compare Sale Pricelists""",

    'description': """
        Long description of module's purpose
    """,

    'author': "CTWW",
    'license': 'OPL-1',
    'website': "https://www.linkedin.com/in/ngo-manh-70a68b183/",
    'category': 'Sales',
    'version': '12.0.1.0.1',
    'depends': ['base', 'sale'],
    'data': [
        'security/ir.model.access.csv',
        'report/compare_sale_pricelists.xml',
    ],
    'demo': [
    ],
    'images': ['static/description/main_screenshot.png'],

}
