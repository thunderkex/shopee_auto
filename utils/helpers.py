import time
import functools
from utils.logger import logger

# Retry decorator for transient errors
def retry(exceptions, tries=3, delay=2, backoff=2):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            _tries, _delay = tries, delay
            while _tries > 1:
                try:
                    return func(*args, **kwargs)
                except exceptions as e:
                    logger.warning(f"{func.__name__} failed: {e}, retrying in {_delay}s...")
                    time.sleep(_delay)
                    _tries -= 1
                    _delay *= backoff
            return func(*args, **kwargs)
        return wrapper
    return decorator

# Helper to extract product/model IDs from Shopee product URL
def parse_product_url(url):
    # Example: https://shopee.co.id/product/123456789/987654321
    import re
    m = re.search(r'/product/(\d+)/(\d+)', url)
    if m:
        return m.group(1), m.group(2)
    return None, None
