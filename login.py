import requests
import random
import hashlib

def random_str(length):
    character='ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789'
    return ''.join((random.choice(character) for i in range(length)))
def encrypt_pass(password):
    sha_signature = \
        hashlib.sha256((hashlib.md5(password.encode()).hexdigest()).encode()).hexdigest()
    return sha_signature
def go():
    username = ''
    password = ''
    r = requests.Session()

    response = r.get('https://shopee.co.id/api/v2/login')
    csrftoken_gen = random_str(32)
    cookie_string = "; ".join([str(x)+"="+str(y) for x,y in response.cookies.get_dict().items()])
    headers = {
        'user-agent'     : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36',
        'x-csrftoken'     : csrftoken_gen,
        'x-requested-with': 'XMLHttpRequest',
        'referer'         : 'https://shopee.co.id',
        'cookie'          : "csrftoken=" + csrftoken_gen + "; " + cookie_string + "SPC_CDS=" + "1"
    }
    #cek data response
    cart_url = 'https://shopee.co.id/api/v1/account_info/?need_cart=1&skip_address=1'
    go_cart = r.get(cart_url, headers=headers, verify=False)
    #print(go_cart)
    recommend_url = 'https://shopee.co.id/api/v2/recommendation/hot_search_words?limit=8&offset=0'
    go_res = r.get(recommend_url, headers=headers, verify=False)
    #print(go_res)
    if go_cart.status_code == 200 and go_res.status_code == 200:
        url="https://shopee.co.id/api/v2/authentication/login"
        response = r.request("POST",url,headers=headers, data = '{"email":"' + username + '","password":"' + encrypt_pass(password) + '","support_whats_app":true}')
        call_user = r.request("get","https://shopee.co.id/api/v2/user/profile/get/")
        user = call_user.json()
        status = user['error']
        print(status)
        print(call_user.status_code)
        if status == None:
            print('Sucessful Login')
        else:
            print('Incorrect email or password')
    else:
        print('salah data cok')
if __name__ == '__main__':
    #jgn lupa masukkan user & pass
    go()