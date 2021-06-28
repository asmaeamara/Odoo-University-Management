# -*- coding: utf-8 -*-

from odoo import models, fields, api

class UniversityClassroom(models.Model):
    _name = 'university.classroom'
    _description = "Classroom entity"

    # department's properties
    name = fields.Char()
    code = fields.Char()