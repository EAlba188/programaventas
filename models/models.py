# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import datetime

class Producto(models.Model):
    _name = 'programaventas.producto'

    id = fields.Char(required=True, size=20, string="ID")
    nombre = fields.Char(string="nombre")
    precio = fields.Float(string="precio", digits=(6,2))
    numeroVentas = fields.Integer(readonly=1, string="Numero Ventas")
    brutoGenerado = fields.Float(string="Bruto Total", readonly=1, default=0)

    @api.depends
    def calcularVentas(self):
        res = 0
        for venta in Venta:
            if (self.id==venta.idproducto):
                res=res+1
        self.numeroVentas=res


class Venta(models.Model):                  #añadir forma de pago
    _name = 'programaventas.venta'

    #CREAR NUMERO DE REFERENCIA AUTOINCREMENTAL
    precio = fields.Float(string="Precio", digits=(6,2), readonly=1)
    dni = fields.Many2one('programaventas.cliente', string="Cliente")
    idproducto = fields.Many2one('programaventas.producto', string="Producto")
    fecha = fields.Date(string="Fecha", default=datetime.today(), readonly=1)
    pago = fields.Float(string="Precio pagado")

    @api.onchange('idproducto')
    def setPrecio(self):
        for producto in Producto:
            if self.idproducto == producto.id:
                self.precio=producto.precio


class Cliente(models.Model):
    _name = 'programaventas.cliente'

    dni = fields.Char(required=True, string="DNI Cliente")
    nombre = fields.Char(string="Nombre")
    numeroCompras = fields.Integer(readonly=1, string="Numero de compras", default=0)
    brutoGenerado = fields.Float(string="Bruto Total", readonly=1, default=0)


class Historico(models.Model):
    _name = 'programaventas.historico'

    #ID del producto
    #Nombre del producto
    #Fecha de la venta
    #precio de la venta
    #dineroBrutoGenerado en todas las ventas del momento
