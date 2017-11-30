# -*- coding: utf-8 -*-
# © 2017 - TODAY Edi Santoso <repodevs@gmail.com>
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl.html)
from odoo import api, fields, models


class TrainingTopic(models.Model):
    _name = 'training.topic'

    training_id = fields.Many2one('training.training', 'Training Topic',
                                  required=True)
    name = fields.Char(string='Name', required=True)
    duration = fields.Float(string='Durasi')
    description = fields.Html(string='Deskripsi')
