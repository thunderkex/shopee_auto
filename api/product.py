from session import ShopeeSession
from utils.logger import logger
from utils.helpers import parse_product_url, retry

@retry(Exception, tries=3)
def get_product_detail(session: ShopeeSession, product_url: str):
    shop_id, item_id = parse_product_url(product_url)
    if not shop_id or not item_id:
        logger.error('Invalid product URL.')
        return None
    url = f'https://{session.get_domain()}/api/v4/item/get'
    payload = {'itemid': int(item_id), 'shopid': int(shop_id)}
    logger.info(f'Fetching product details for shop_id={shop_id}, item_id={item_id}')
    resp = session.post(url, json=payload)
    if resp.status_code == 200:
        return resp.json().get('data')
    logger.error(f'Failed to fetch product details: {resp.text}')
    return None
