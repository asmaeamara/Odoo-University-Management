# -*- coding: utf-8 -*-

from odoo import models, fields, api

class UniversityStudent(models.Model):
    _name = 'university.student'
    _description = "Student entity"

    # student's properties
    f_name = fields.Char('First name')
    l_name = fields.Char('Last name')
    gender = fields.Selection([('male', 'Male'), ('female', 'Female')])
    identity_card = fields.Char('Identity card')
    address = fields.Char('Address')
    birthday = fields.Date('Birthday')
    registration_date = fields.Date('Registration date')
    email = fields.Char('Email')
    phone = fields.Char('Phone')