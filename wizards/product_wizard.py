
from odoo import models, fields, api


class ProductWizard(models.TransientModel):
    _name = "product.wizard"

    def _get_default_products(self):
        return self.env['programaventas.producto'].browse(self.env.context.get('active_ids'))

    idproductos = fields.Many2many("programaventas.producto",string="Productos", default=_get_default_products)
    euros = fields.Float(string="Aumento de precio")

    @api.multi
    def increasePrice(self):
        for x in self:
            if x.idproductos:
                for y in x.idproductos:
                    y.precio+=x.precio