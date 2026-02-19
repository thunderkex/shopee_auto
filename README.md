# Shopee Automation

**WARNING: This project is for educational purposes only. Automating Shopee interactions violates their Terms of Service and may result in account suspension or legal action. Use at your own risk.**

## Features
- Login (manual captcha fallback)
- Product search & add to cart
- Initiate checkout (stops before final order)
- Fully script-based, no Selenium/webdriver

## Setup
1. Clone this repo.
2. Copy `.env.example` to `.env` and fill in your credentials and product URL.
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the script:
   ```bash
   python main.py
   ```

## How it Works
- Uses direct HTTP requests to Shopee's backend APIs (`shopee.co.id`).
- Mimics browser headers and manages cookies/tokens.
- Handles anti-bot measures as much as possible (manual captcha fallback).

## Limitations
- Captcha and advanced anti-bot protections may block automation.
- For educational use only.

## Project Structure
```
shopee_auto_http/
├── main.py
├── config.py
├── session.py
├── api/
│   ├── auth.py
│   ├── cart.py
│   ├── product.py
│   └── checkout.py
├── utils/
│   ├── logger.py
│   └── helpers.py
├── tests/
├── .env.example
├── requirements.txt
└── README.md
```
