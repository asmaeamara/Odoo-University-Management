# -*- coding: utf-8 -*-

from odoo import models, fields, api

class UniversityDepartment(models.Model):
    _name = 'university.department'
    _description = "Department entity"

    # department's properties
    name = fields.Char()
    code = fields.Char()