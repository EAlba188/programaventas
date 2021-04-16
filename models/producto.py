
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

    @api.depends("ventas")
    def actualizarProducto(self):
        productos = self.env['programaventas.producto'].search([])
        for x in productos:
            busqueda = self.env['programaventas.venta'].search([('idproducto.id', '=', x.id)])
            numeroVentas=0
            brutoGenerado=0
            if(len(busqueda)>0):
                for i in busqueda:
                    numeroVentas += i.unidades
                    brutoGenerado += i.precio
                x.numeroVentas=numeroVentas
                x.brutoGenerado=brutoGenerado
            else:
                x.numeroVentas = 0
                x.brutoGenerado = 0


    id = fields.Char(required=True, size=20, string="ID")   #si le das id se hace solo???
    name = fields.Char(string="Nombre Producto")
    precio = fields.Float(string="Precio", digits=(6,2))
    numeroVentas = fields.Integer(string="Numero Ventas", compute=actualizarProducto, store="true")
    brutoGenerado = fields.Float(string="Bruto Total", default=0, compute=actualizarProducto, store="true")
    ventas = fields.One2many("programaventas.venta", "idproducto")