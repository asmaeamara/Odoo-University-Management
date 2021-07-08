# -*- coding: utf-8 -*-

from odoo import models, fields, api

class UniversityProfessor(models.Model):
    _name = 'university.professor'
    _description = "Professor entity"

    # professor's properties
    f_name = fields.Char('First name')
    l_name = fields.Char('Last name')
    gender = fields.Selection([('male', 'Male'), ('female', 'Female')])
    identity_card = fields.Char('Identity card')
    address = fields.Char('Address')
    birthday = fields.Date('Birthday')
    start_date = fields.Date('Start date')
    email = fields.Char('Email')
    phone = fields.Char('Phone')

    # professor's relationships
    department_id = fields.Many2one(comodel_name='university.department')
    subject_id = fields.Many2one(comodel_name='university.subject')
    classroom_ids = fields.Many2many(comodel_name='university.classroom',
                                     relation='professor_classroom_rel',
                                     column1='f_name',
                                     column2='classroom_name')


    # Get professor names
    # Result : professor window / [Math Informatique Department] Rachid SomeOne
    @api.multi
    def name_get(self):
        result = []
        for professor in self:
            name = '['+ professor.department_id.department_name + '] ' + professor.f_name + ' ' +professor.l_name
            result.append((professor.id, name))

        return result