# -*- coding: utf-8 -*-
# © 2017 - TODAY Edi Santoso <repodevs@gmail.com>
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl.html)

from odoo import fields, models


class ResUsers(models.Model):
	_inherit = 'res.users'

	api_key = fields.Char(string="API KEY", size=32)