# -*- coding: utf-8 -*-

from odoo import models, fields, api

class UniversityClassroom(models.Model):
    _name = 'university.classroom'
    _description = "Classroom entity"

    # department's properties
    classroom_name = fields.Char(string='name')
    code = fields.Char()

    # classroom's relationships
    student_ids = fields.One2many(comodel_name='university.student', inverse_name='classroom_id')
    professor_ids = fields.Many2many(comodel_name='university.professor',
                                     relation='classroom_professor_rel',
                                     column1='classroom_name',
                                     column2='f_name')
    subject_ids = fields.Many2many(comodel_name='university.subject',
                                   relation='classroom_subject_rel',
                                   column1='classroom_name',
                                   column2='subject_name')