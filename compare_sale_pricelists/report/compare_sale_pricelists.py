# -*- coding: utf-8 -*-
from odoo import api, fields, models, tools


class CompareSalePricelist(models.Model):
    _name = "compare.sale.pricelist"
    _auto = False
    _order = 'categ_id'

    product_id = fields.Many2one('product.product', 'Product', readonly=True)
    categ_id = fields.Many2one('product.category', 'Product Category', readonly=True)
    fixed_price = fields.Float('Price', group_operator="avg")
    date_start = fields.Date('Date Start')
    pricelist_name = fields.Char('Pricelist Name')

    @api.model_cr
    def init(self):
        tools.drop_view_if_exists(self._cr, self._table)
        self.env.cr.execute("""CREATE or REPLACE VIEW %s as (

            SELECT MIN(ppi.id) AS id,
                   CASE WHEN ppi.product_id IS NOT NULL THEN ppi.product_id
                    WHEN ppi.product_tmpl_id IS NOT NULL THEN pp.id ELSE NULL END AS product_id,
                   CASE WHEN ppi.product_id IS NOT NULL THEN pt2.categ_id
                    WHEN ppi.product_tmpl_id IS NOT NULL THEN pt.categ_id ELSE NULL END AS categ_id,
                   ppi.fixed_price,
                   ppi.date_start,
                   p.name AS pricelist_name
            FROM product_pricelist_item ppi
                LEFT JOIN product_pricelist p ON ppi.pricelist_id = p.id
                LEFT JOIN product_product pp ON ppi.product_tmpl_id = pp.product_tmpl_id
                LEFT JOIN product_template pt ON ppi.product_tmpl_id = pt.id
                LEFT JOIN product_product pp2 ON ppi.product_id = pp2.id
                LEFT JOIN product_template pt2 ON pp2.product_tmpl_id = pt2.id
            WHERE ppi.compute_price = 'fixed'
              AND ppi.applied_on IN ('0_product_variant', '1_product')
            GROUP BY ppi.id, pp.id, p.name, pt2.categ_id, pt.categ_id
            ORDER BY ppi.id, ppi.product_id, ppi.date_start DESC

        )""" % (self._table,))
