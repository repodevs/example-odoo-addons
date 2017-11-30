# -*- coding: utf-8 -*-
# © 2017 - TODAY Edi Santoso <repodevs@gmail.com>
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl.html)
{
    'name': 'Training App',
    'author': 'Edi Santoso <me@repodevs.com>',
    'summary': 'Module Untuk Training Management',
    'version': '10.1.0.0',
    'category': 'Training',
    'website': 'https://me.repodevs.com',
    'description': """
Module Untuk Training Management
================================
* Daftar Kelas
* Daftar Materi Training
* Daftar Topic Training
* Daftar Peserta
* Soon..
""",
    'depends': ['base'],
    'data': [
        # menu
        'views/training_menu.xml',
        # views
        'views/training_views.xml',
        'views/training_topic_views.xml',
        # view api
        'views/res_users.xml',
    ],
    'installable': True,
}
