import requests
import random
import hashlib
import json
import requests_random_user_agent

def random_str(length):
    character='ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789'
    return ''.join((random.choice(character) for i in range(length)))
def encrypt_pass(password):
    sha_signature = \
    hashlib.sha256((hashlib.md5(password.encode()).hexdigest()).encode()).hexdigest()
    return sha_signature

r = requests.Session()
r.headers['User-Agent']
username = 'EMAIL MU'
password = 'PASWORD MU'
response = r.get('https://shopee.co.id/api/v2/login')
csrftoken_gen = random_str(32)
crsf_login = csrftoken_gen
cookie_string = "; ".join([str(x)+"="+str(y) for x,y in response.cookies.get_dict().items()])
# <<<<<<<<<<<<<< Start Login Code >>>>>>>>>>>>>>>>
headers = {
        # 'user-agent'     : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36',
        'x-csrftoken'     : crsf_login,
        'x-requested-with': 'XMLHttpRequest',
        'referer'         : 'https://shopee.co.id',
        'cookie'          : "csrftoken=" + crsf_login + "; " + cookie_string + "SPC_CDS=" + "1"
    }
url="https://shopee.co.id/api/v2/authentication/login"
response2 = r.request("POST",url,headers=headers, data = '{"email":"' + username + '","password":"' + encrypt_pass(password) + '","support_whats_app":true}')
cookie_string2 = "; ".join([str(x)+"="+str(y) for x,y in response2.cookies.get_dict().items()])
# <<<<<<<<<<<<<< End Login Code >>>>>>>>>>>>>>>>

# <<<<<<<<<<<<<< Check Login Info Code >>>>>>>>>>>>>>>>
call_user = r.request("get","https://shopee.co.id/api/v2/user/profile/get/")
user = call_user.json()
status = user['error']
print(status)
print(call_user.status_code)
if status == None:
    print('Sucessful Login')
else:
    print('Incorrect email or password')
    # EXAMPLE OTP
#     print('Trying with OTP Code')
# cokee = {'cookie':"csrftoken=" + crsf_login + "; " + cookie_string2}
# token_csrf = crsf_login
# r.cookies.update(cokee)
# print('Send OTP code To your whatsapp number')
# url="https://shopee.co.id/api/v2/authentication/resend_otp"
# response2 = r.request("POST",url,headers=headers, data = '{"operation":5,"channel":3,"support_whats_app":true,"force_channel":true}')
# print(response2.status_code)
# data = input("Please enter a Verif code: ")
# url="https://shopee.co.id/api/v2/authentication/vcode_login"
# response2 = r.request("POST",url,headers=headers, data = '{"email":"","otp":"'+ data +'"}')
# print(response2.status_code)
# print('Lets Run')
# <<<<<<<<<<<<<< End Login Info Code >>>>>>>>>>>>>>>>

# <<<<<<<<<<<<<< Add To Cart Code >>>>>>>>>>>>>>>>
cokee = {'cookie':"csrftoken=" + crsf_login + "; " + cookie_string2}
token_csrf = crsf_login
r.cookies.update(cokee)
sp_header = {'referer': 'https://shopee.co.id/',
             'content-type': 'application/json',
             'x-csrftoken' : token_csrf,
             'x-requested-with':'XMLHttpRequest',
             'x-shopee-language':'id'}
r.headers.update(sp_header)
payload1 = {
"quantity":1,
"checkout":True,
"update_checkout_only":False,
"donot_add_quantity":False,
"source":"{\"refer_urls\":[]}",
"client_source":1,
# "add_on_deal_id":deal id,
"shopid":5843062, #dapet dari item model
"itemid":7857362237, #dapet dari split product
"modelid":51773057051, #dapet dari split product
}
response = r.post('https://shopee.co.id/api/v2/cart/add_to_cart', data=json.dumps(payload1))
print(payload1)
print(response)
print(response.content)
# <<<<<<<<<<<<<< End Add To Cart Code >>>>>>>>>>>>>>>>