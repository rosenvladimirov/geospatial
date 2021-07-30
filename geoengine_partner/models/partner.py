# Copyright 2011-2017 Camptocamp SA
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl)

from odoo import fields, models, api, _

import logging
_logger = logging.getLogger(__name__)


class ResPartner(models.Model):
    """Add geo_point to partner using a function field"""
    _inherit = "res.partner"

    geo_point = fields.GeoPoint("Address coordinates")

    @api.multi
    def geo_localize(self):
        res = super(ResPartner, self).geo_localize()
        for record in self:
            if not record.partner_latitude or not record.partner_longitude:
                record.geo_point = False
            else:
                record.geo_point = fields.GeoPoint.from_latlon(record.env.cr, record.partner_latitude, record.partner_longitude)
            _logger.info("GEO %s" % record.geo_point)
        return res
