# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import datetime

class Producto(models.Model):
    _name = 'programaventas.producto'

    id = fields.Char(required=True, size=20, string="ID")
    name = fields.Char(string="Nombre Producto")
    precio = fields.Float(string="Precio", digits=(6,2))
    numeroVentas = fields.Integer(readonly=1, string="Numero Ventas")
    brutoGenerado = fields.Float(string="Bruto Total", readonly=1, default=0)

    def sumarVentas(self):
        self.numeroVentas+=1



class Venta(models.Model):
    _name = 'programaventas.venta'


    #CREAR NUMERO DE REFERENCIA AUTOINCREMENTAL
    #Añadir descuentos?
    dni = fields.Many2one('programaventas.cliente', string="Cliente")
    unidades = fields.Integer(string="Cantidad")
    idproducto = fields.Many2one('programaventas.producto', string="Producto")
    precio = fields.Float(invisible=True)
    precio_copia = fields.Float(string="Precio Total", readonly=1)
    precioUnitario = fields.Float(string="Precio unitario", readonly=1, related='idproducto.precio', default=0)
    fecha = fields.Date(string="Fecha", default=datetime.today(), readonly=1)
    pago = fields.Selection(string="Forma de pago", selection=[('efectivo',"Efectivo"),('tarjeta',"Tarjeta")])

    @api.onchange('unidades')
    def setUnits(self):
        self.precio_copia = self.unidades * self.precioUnitario
        self.precio = self.unidades * self.precioUnitario
        #self.precio=self.unidades*self.idproducto.precio - another option

    @api.onchange('unidades')
    def actualizarProducto(self):
        self.idproducto.numeroVentas+=self.unidades
        #el problema es que si borramos el registro no cambia ya el numero en la zona productos
        self.idproducto.brutoGenerado=self.idproducto.numeroVentas*self.idproducto.precio





class Cliente(models.Model):
    _name = 'programaventas.cliente'

    dni = fields.Char(required=True, string="DNI Cliente", size=9)
    name = fields.Char(string="Nombre")
    numeroCompras = fields.Integer(readonly=1, string="Numero de compras", default=0)
    brutoGenerado = fields.Float(string="Bruto Total", readonly=1, default=0)


class Historico(models.Model):
    _name = 'programaventas.historico'

    #ID del producto
    #Nombre del producto
    #Fecha de la venta
    #precio de la venta
    #dineroBrutoGenerado en todas las ventas del momento
