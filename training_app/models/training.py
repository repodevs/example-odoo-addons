# -*- coding: utf-8 -*-
# © 2017 - TODAY Edi Santoso <repodevs@gmail.com>
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl.html)
from odoo import api, fields, models


class TrainingApp(models.Model):
    _name = 'training.training'
    _description = 'base training app'

    name = fields.Char(string='Name', index=True, required=True)
    active = fields.Boolean(string='Active', default=True)
    description = fields.Text(string='Deskripsi')
    trainer_ids = fields.Many2many('res.users', string='Trainer(s)')
    topic_ids = fields.One2many('training.topic', 'training_id')
    state = fields.Selection([
        ('draft', 'Draft'), ('cancel', 'Cancel'),
        ('onprogress', 'On Progress'), ('done', 'Done')],
        string='Status', copy=False, default='draft', index=True, readonly=True)
