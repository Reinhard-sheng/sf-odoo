from odoo import http

class WechartApi(http.Controller):
    @http.route('/api/smart-farm/banner/list', type='json', auth="public")
    def get_banner_list(self):
        return {
            'data': {
                'code': 200,
                'data': []
            }
        }
