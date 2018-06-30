from odoo import http


class WechartApi(http.Controller):
    @http.route('/api/smart-farm/banner/list', type='json', auth="none")
    def get_banner_list(self):
        return {
            'data': {
                'code': 200,
                'data': [
                    {
                        'businessId': 1,
                        'picUrl': 'https://www.baidu.com/img/bd_logo1.png',
                    },
                    {
                        'businessId': 2,
                        'picUrl': 'https://www.baidu.com/img/bd_logo1.png',
                    },
                    {
                        'businessId': 3,
                        'picUrl': 'https://www.baidu.com/img/bd_logo1.png',
                    },
                ]
            }
        }

    @http.route('/shop/goods/category/all', type='json', auth="none")
    def get_category_all(self):
        return {
            'data': {
                'code': 200,
                'data': [
                    {
                        'id': 1,
                        'name': '白菜',
                    },
                    {
                        'id': 2,
                        'name': '生菜',
                    },
                    {
                        'id': 3,
                        'name': '菠菜',
                    },
                ]
            }
        }
