# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import datetime


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
