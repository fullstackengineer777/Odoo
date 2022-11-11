# -*- coding: utf-8 -*-
{
  'name': 'School Management',
  'version': '15.0.1.0.0',
  'category': '',
  'author': 'Cybrosys Techno Solutions',
  'website': "https://www.cybrosys.com",
  'company': 'Cybrosys Techno Solutions',
  'maintainer': 'Cybrosys Techno Solutions',
  'summary': 'Record Student Details',
  "description": """To manage School""",
  'depends': ['base'],
   'data': [
      'security/ir.model.access.csv',
      'views/student_views.xml',
  ],
  'qweb': [],
  "license": "AGPL-3",
  'installable': True,
  'auto_install': False,
}