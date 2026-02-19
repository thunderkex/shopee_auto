import os
from dotenv import load_dotenv

load_dotenv()

SHOPEE_USERNAME = os.getenv('SHOPEE_USERNAME')
SHOPEE_PASSWORD = os.getenv('SHOPEE_PASSWORD')
SHOPEE_DOMAIN = os.getenv('SHOPEE_DOMAIN', 'shopee.co.id')
PRODUCT_URL = os.getenv('PRODUCT_URL')
