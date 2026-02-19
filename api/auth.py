from session import ShopeeSession
from config import SHOPEE_USERNAME, SHOPEE_PASSWORD
from utils.logger import logger
from utils.helpers import retry

@retry(Exception, tries=3)
def login(session: ShopeeSession):
    url = f'https://{session.get_domain()}/api/v4/account/login/'
    payload = {
        'login_key': SHOPEE_USERNAME,
        'password': SHOPEE_PASSWORD,
    }
    logger.info(f'Attempting login for {SHOPEE_USERNAME}')
    resp = session.post(url, json=payload)
    if resp.status_code == 200 and resp.json().get('error') == 0:
        logger.info('Login successful.')
        # Extract CSRF token from cookies if present
        csrf = resp.cookies.get('csrftoken')
        if csrf:
            session.update_csrf_token(csrf)
        return True
    elif 'captcha' in resp.text:
        logger.warning('Captcha required. Please login manually and update cookies.')
        return False
    else:
        logger.error(f'Login failed: {resp.text}')
        return False
