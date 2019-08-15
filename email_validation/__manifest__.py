
# -*- coding: utf-8 -*-
###############################################################################
#
#    Odoo, Open Source Management Solution
#
#    Copyright (c) All rights reserved:
#        (c) 2015  TM_FULLNAME
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see http://www.gnu.org/licenses
#
###############################################################################
{
    'name': 'Email Validation',
    'summary': 'Email Validation',
    'version': '1.0',
    'description': """Email Validation""",
    'author': 'Ananthu Krishna',
    'maintainer': 'Ananthu Krishna',
    'website': 'http://www.codersfort.com',
    "images": ["images/Banner.png"],
    'license': 'AGPL-3',
    'category': 'General',
    'depends': ['base','web'],
    'data': [
        'views/assets.xml'
    ],
    'qweb': ['static/src/xml/ninebox.xml'],
    'installable': True,
    'application': True,
    
}