from session import ShopeeSession
from utils.logger import logger
from utils.helpers import retry

@retry(Exception, tries=3)
def get_checkout_info(session: ShopeeSession):
    url = f'https://{session.get_domain()}/api/v4/checkout/get'
    resp = session.post(url, json={})
    if resp.status_code == 200:
        return resp.json().get('data')
    logger.error(f'Failed to get checkout info: {resp.text}')
    return None

@retry(Exception, tries=3)
def place_order(session: ShopeeSession, checkout_payload: dict):
    url = f'https://{session.get_domain()}/api/v4/checkout/place_order'
    logger.info('Placing order (simulation, not final step).')
    resp = session.post(url, json=checkout_payload)
    if resp.status_code == 200:
        logger.info('Order placed (simulation).')
        return resp.json()
    logger.error(f'Failed to place order: {resp.text}')
    return None
