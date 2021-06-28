# -*- coding: utf-8 -*-

from odoo import models, fields, api

class UniversitySubject(models.Model):
    _name = 'university.subject'
    _description = "Subject entity"

    # department's properties
    name = fields.Char()
    code = fields.Char()