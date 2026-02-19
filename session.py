import requests
from utils.logger import logger

class ShopeeSession:
    def __init__(self):
        self.session = requests.Session()
        self.base_url = f'https://{self.get_domain()}/api/v4/'
        self.set_default_headers()

    def get_domain(self):
        from config import SHOPEE_DOMAIN
        return SHOPEE_DOMAIN

    def set_default_headers(self):
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
            'Accept': 'application/json, text/plain, */*',
            'Accept-Language': 'en-US,en;q=0.9',
            'Referer': f'https://{self.get_domain()}/',
            'Connection': 'keep-alive',
        })
        logger.info('Default headers set for Shopee session.')

    def update_csrf_token(self, token):
        self.session.headers.update({'X-CSRFToken': token})

    def get(self, url, **kwargs):
        return self.session.get(url, **kwargs)

    def post(self, url, data=None, json=None, **kwargs):
        return self.session.post(url, data=data, json=json, **kwargs)
