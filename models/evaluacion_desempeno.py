from odoo import models,fields,api

class EvaluacionDesempeno(models.Model):

    _name = 'evaluacion.desempeno'
    _description = 'Desempeño del empleado'
    title = fields.Char(string = 'Titulo',required = True)
    employee = fields.Many2one('res.users', string="Empleado", required=True)
    date = fields.Date(string = 'Fecha de evaluación',required = True)
    comments = fields.Text(string = 'Comentarios')
    score = fields.Selection([
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
        ('6', '6'),
        ('7', '7'),
        ('8', '8'),
        ('9', '9'),
        ('10', '10')
    ], string="Puntuación", required=True)
    


    state = fields.Selection([
        ('pending','Pendiente'),
        ('in_progress', 'En progreso'),
        ('done', 'Finalizado'),
    ], string='Estado', default= 'pending')

