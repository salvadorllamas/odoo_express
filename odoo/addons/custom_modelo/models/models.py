# -*- coding: utf-8 -*-

from odoo import models, fields, api



class Todo(models.Model):
    _name = 'wb.todo'
    name=fields.Char('Nombre')
    description = fields.Text('Descripcion')
    numberTasks=fields.Integer('Tareas')
    status=fields.Selection(selection=[('borradas','Borradas'),('hechas','Hechas'),('pendientes','Pendientes')])
    
