from config import PRODUCT_URL
from session import ShopeeSession
from api import auth, product, cart, checkout
from utils.logger import logger


def main():
    session = ShopeeSession()
    # 1. Login
    if not auth.login(session):
        logger.error('Login failed or captcha required. Exiting.')
        return

    # 2. Get product details
    prod = product.get_product_detail(session, PRODUCT_URL)
    if not prod:
        logger.error('Could not fetch product details. Exiting.')
        return
    shop_id = prod['shopid']
    item_id = prod['itemid']
    # Pick first model (variant) for demo
    model_id = prod['models'][0]['modelid'] if prod.get('models') else None
    if not model_id:
        logger.error('No model found for product. Exiting.')
        return

    # 3. Add to cart
    if not cart.add_to_cart(session, shop_id, item_id, model_id):
        logger.error('Failed to add to cart. Exiting.')
        return

    # 4. Get cart and checkout info
    cart_data = cart.get_cart(session)
    checkout_info = checkout.get_checkout_info(session)
    logger.info(f'Cart: {cart_data}')
    logger.info(f'Checkout info: {checkout_info}')

    # 5. (Optional) Place order (simulation only)
    # Uncomment below to simulate order placement (WILL NOT CONFIRM ORDER)
    # result = checkout.place_order(session, checkout_info)
    # logger.info(f'Order result: {result}')

if __name__ == '__main__':
    main()
