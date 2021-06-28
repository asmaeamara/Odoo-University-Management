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