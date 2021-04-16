
from odoo import models, fields, api
from datetime import datetime

class Cliente(models.Model):
    _name = 'programaventas.cliente'

    @api.depends("ventas")
    def actualizarCliente(self):
        clientes = self.env['programaventas.cliente'].search([])
        ventas = self.env['programaventas.venta'].search([])
        for x in clientes:
            brutoGenerado=0
            numeroCompras=0
            for i in ventas:
                if i.dni.dni == x.dni:
                    brutoGenerado += i.precio
                    numeroCompras += i.unidades
            x.brutoGenerado=brutoGenerado
            x.numeroCompras=numeroCompras

    dni = fields.Char(required=True, string="DNI Cliente", size=9)
    name = fields.Char(string="Nombre")
    numeroCompras = fields.Integer(readonly=1, string="Numero de compras", default=0, compute=actualizarCliente, store="true")
    brutoGenerado = fields.Float(string="Bruto Total", readonly=1, default=0, compute=actualizarCliente, store="true")
    ventas = fields.One2many("programaventas.venta", "dni")


