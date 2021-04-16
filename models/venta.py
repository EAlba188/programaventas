
from odoo import models, fields, api
from datetime import datetime


class Venta(models.Model):
    _name = 'programaventas.venta'

    @api.depends('unidades', 'precioUnitario','dni')
    def actualizarTotal(self):

        for x in self:
            x.precio=x.unidades*x.precioUnitario

            #self.env['programaventas.producto'].browse(1) elemento
            #self.env['programaventas.producto'].search([("name","=","nombreProducto")]) lista





    #CREAR NUMERO DE REFERENCIA AUTOINCREMENTAL
    #Añadir descuentos?
    dni = fields.Many2one('programaventas.cliente', string="Cliente")
    unidades = fields.Integer(string="Cantidad")
    idproducto = fields.Many2one('programaventas.producto', string="Producto")
    precio = fields.Float(compute=actualizarTotal, store="true")
    precioUnitario = fields.Float(string="Precio unitario", readonly=1, related='idproducto.precio', default=0)
    fecha = fields.Date(string="Fecha", default=datetime.today(), readonly=1)
    pago = fields.Selection(string="Forma de pago", selection=[('efectivo',"Efectivo"),('tarjeta',"Tarjeta")])

