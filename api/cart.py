from session import ShopeeSession
from utils.logger import logger
from utils.helpers import retry

@retry(Exception, tries=3)
def add_to_cart(session: ShopeeSession, shop_id: int, item_id: int, model_id: int, quantity: int = 1):
    url = f'https://{session.get_domain()}/api/v4/cart/add'
    payload = {
        'shopid': shop_id,
        'itemid': item_id,
        'modelid': model_id,
        'quantity': quantity
    }
    logger.info(f'Adding to cart: shop_id={shop_id}, item_id={item_id}, model_id={model_id}, qty={quantity}')
    resp = session.post(url, json=payload)
    if resp.status_code == 200 and resp.json().get('error') == 0:
        logger.info('Item added to cart.')
        return True
    logger.error(f'Failed to add to cart: {resp.text}')
    return False

@retry(Exception, tries=3)
def get_cart(session: ShopeeSession):
    url = f'https://{session.get_domain()}/api/v4/cart/get'
    resp = session.post(url, json={})
    if resp.status_code == 200:
        return resp.json().get('data')
    logger.error(f'Failed to fetch cart: {resp.text}')
    return None
