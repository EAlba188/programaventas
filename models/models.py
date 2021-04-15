# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import datetime

class Producto(models.Model):
    _name = 'programaventas.producto'


    def write(self, values):
        producto_write = super(Producto, self).write(values)

        historico = {
            'producto': self.id,
            'name': self.name,
            'precio': self.precio,
            'fecha': datetime.today()
        }
        self.env['programaventas.historico'].create(historico)

        return producto_write



    def actualizarProducto(self):
        productos = self.env['programaventas.producto'].search([])
        for x in productos:
            busqueda = self.env['programaventas.venta'].search([('idproducto.id', '=', x.id)])
            x.numeroVentas=0
            x.brutoGenerado=0
            if(len(busqueda)>0):
                for i in busqueda:
                    x.numeroVentas += i.unidades
                    x.brutoGenerado += i.precio
            else:
                x.numeroVentas = 0
                x.brutoGenerado = 0


    id = fields.Char(required=True, size=20, string="ID")   #si le das id se hace solo???
    name = fields.Char(string="Nombre Producto")
    precio = fields.Float(string="Precio", digits=(6,2))
    numeroVentas = fields.Integer(string="Numero Ventas", compute=actualizarProducto, store="true")
    brutoGenerado = fields.Float(string="Bruto Total", default=0, compute=actualizarProducto, store="true")





class Venta(models.Model):
    _name = 'programaventas.venta'

    @api.depends('unidades', 'precioUnitario','dni')
    def actualizarTotal(self):

        for x in self:
            x.precio=x.unidades*x.precioUnitario

            #self.env['programaventas.producto'].browse(1) elemento
            #self.env['programaventas.producto'].search([("name","=","nombreProducto")]) lista

        self.idproducto.actualizarProducto()
        self.dni.actualizarCliente()




    #CREAR NUMERO DE REFERENCIA AUTOINCREMENTAL
    #Añadir descuentos?
    dni = fields.Many2one('programaventas.cliente', string="Cliente")
    unidades = fields.Integer(string="Cantidad")
    idproducto = fields.Many2one('programaventas.producto', string="Producto")
    precio = fields.Float(compute=actualizarTotal, store="true")
    precioUnitario = fields.Float(string="Precio unitario", readonly=1, related='idproducto.precio', default=0)
    fecha = fields.Date(string="Fecha", default=datetime.today(), readonly=1)
    pago = fields.Selection(string="Forma de pago", selection=[('efectivo',"Efectivo"),('tarjeta',"Tarjeta")])


class Cliente(models.Model):
    _name = 'programaventas.cliente'


    def actualizarCliente(self):
        clientes = self.env['programaventas.cliente'].search([])
        ventas = self.env['programaventas.venta'].search([])
        for x in clientes:
            x.brutoGenerado=0
            x.numeroCompras=0
            for i in ventas:
                if i.dni.dni == x.dni:
                    x.brutoGenerado += i.precio
                    x.numeroCompras += i.unidades

    dni = fields.Char(required=True, string="DNI Cliente", size=9)
    name = fields.Char(string="Nombre")
    numeroCompras = fields.Integer(readonly=1, string="Numero de compras", default=0, compute=actualizarCliente, store="true")
    brutoGenerado = fields.Float(string="Bruto Total", readonly=1, default=0, compute=actualizarCliente, store="true")


class Historico(models.Model):
    _name = 'programaventas.historico'


    producto = fields.Char(string="ID Producto")
    name = fields.Char(string="Nombre")
    precio = fields.Float(string="Precio")
    fecha = fields.Date(string="Fecha")


    #ID del producto
    #Nombre del producto
    #Fecha de la venta
    #precio de la venta
    #dineroBrutoGenerado en todas las ventas del momento
    #self write (self vals) return super nombreclase/modelo.write ----nocreate
