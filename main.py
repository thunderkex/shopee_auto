import requests
import random
import hashlib
import json
from configparser import ConfigParser
import time
import re
import time
import requests_random_user_agent
from selenium import webdriver
CONFIG = ConfigParser()
CONFIG.read('config.cok')

usern = CONFIG.get('TEL', 'USERNAME')
pssword = CONFIG.get('TEL', 'PASSWORD')
link = CONFIG.get('TEL', 'LINK')
class gas:

        def __init__(self):
            self.random_str

        def random_str(self, length):
            character='ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789'
            return ''.join((random.choice(character) for i in range(length)))

        def encrypt_pass(self, password):
            sha_signature = \
            hashlib.sha256((hashlib.md5(password.encode()).hexdigest()).encode()).hexdigest()
            return sha_signature

        def parse(self):
            print("Parsing Data URL..")
            regex = r"https://shopee\Wco.id/(.*?)-i.(?P<shop>\d+)\W(?P<item>\d+)"
            for match in re.finditer(regex,link):
                self.iditem = match['item']#Hasil Item ID
                self.idshop = match['shop']#Hasil Shop ID
                print(self.iditem)
                print(self.idshop)
            print("Done..")

        def get_model(self):
            y = requests.Session()
            print("Getting Model Id..")
            call_model = y.request("get","https://shopee.co.id/api/v2/item/get?itemid="+ self.iditem + "&shopid="+ self.idshop)
            model = json.loads(call_model.text)
            # self.get =json.dumps(model['item']['models'][0]['price_stocks'][0]['model_id'])
            self.addon =json.dumps(model['item']['add_on_deal_info'])
            try:
                self.get =json.dumps(model['item']['add_on_deal_info']['add_on_deal_id'])
            except TypeError:
                # self.get is type(None):
                self.get =json.dumps(model['item']['models'][0]['modelid'])
            except TypeError:
                self.get =json.dumps(model['item']['models'][0]['price_stocks'][0]['model_id'])
            print("Is Add On Deal ? = " + self.addon)
            print("Print Model ID = " + self.get)
            y.cookies.clear()
            print("Done..")

        def Login(self):
            print("Logging In..")
            self.r = requests.Session()
            self.r.headers['User-Agent']
            response = self.r.get('https://shopee.co.id/api/v2/login')
            csrftoken_gen = self.random_str(32)
            self.crsf_login = csrftoken_gen
            cookie_string = "; ".join([str(x)+"="+str(y) for x,y in response.cookies.get_dict().items()])
            # <<<<<<<<<<<<<< Start Login Code >>>>>>>>>>>>>>>>
            time.sleep(0.2)
            headers = {
                    # 'user-agent'     : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36',
                    'x-csrftoken'     : self.crsf_login,
                    'x-requested-with': 'XMLHttpRequest',
                    'referer'         : 'https://shopee.co.id',
                    'cookie'          : "csrftoken=" + self.crsf_login + "; " + cookie_string + "SPC_CDS=" + "1"
                }
            url="https://shopee.co.id/api/v2/authentication/login"
            response2 = self.r.request("POST",url,headers=headers, data = '{"email":"' + usern + '","password":"' + self.encrypt_pass(pssword) + '","support_whats_app":true}')
            self.cookie_string2 = "; ".join([str(x)+"="+str(y) for x,y in response2.cookies.get_dict().items()])
            # <<<<<<<<<<<<<< End Login Code >>>>>>>>>>>>>>>>
            time.sleep(0.5)
            print("Check Login Info..")
            # <<<<<<<<<<<<<< Check Login Info Code >>>>>>>>>>>>>>>>
            call_user = self.r.request("get","https://shopee.co.id/api/v2/user/profile/get/")
            user = call_user.json()
            status = user['error']
            print(status)
            print(call_user.status_code)
            if status == None:
                print('Check Login Info finish without error..')
                print('Sucessful Login')
            else:
                print('Incorrect email or password.. . .')
                print('Lemme try again')
                print('Trying with OTP Code')
                cokee = {'cookie':"csrftoken=" + self.crsf_login + "; " + self.cookie_string2}
                self.r.cookies.update(cokee)
                print('Send OTP code To your whatsapp number')
                url="https://shopee.co.id/api/v2/authentication/resend_otp"
                response2 = self.r.request("POST",url,headers=headers, data = '{"operation":5,"channel":3,"support_whats_app":true,"force_channel":true}')
                print(response2.status_code)
                data = input("Please enter a Verif code: ")
                url="https://shopee.co.id/api/v2/authentication/vcode_login"
                response2 = self.r.request("POST",url,headers=headers, data = '{"email":"' + usern + '","otp":"'+ data +'"}')
                print(response2.status_code)
                print('Lets Run')
        # <<<<<<<<<<<<<< End Login Info Code >>>>>>>>>>>>>>>>
        def cek(self):
            path = "C:/geckodriver"
            driver = webdriver.Firefox(executable_path = path)
            driver.get(link)
            while 1:
                if driver.find_elements_by_class_name("btn-solid-primary--disabled"):
                    print("Element exists")
                else:
                    self.add()
                time.sleep(1)
        def add(self):
                # <<<<<<<<<<<<<< Add To Cart Code >>>>>>>>>>>>>>>>
            ids = self.idshop
            idi = self.iditem
            idm = self.get
            cokee = {'cookie':"csrftoken=" + self.crsf_login + "; " + self.cookie_string2}
            token_csrf = self.crsf_login
            self.r.cookies.update(cokee)
            sp_header = {'referer': 'https://shopee.co.id/',
                        'content-type': 'application/json',
                        'x-csrftoken' : token_csrf,
                        'x-requested-with':'XMLHttpRequest',
                        'x-shopee-language':'id'}
            self.r.headers.update(sp_header)
            if self.addon == 'null':
                payload1 = {
                "quantity":1,
                "checkout":True,
                "update_checkout_only":False,
                "donot_add_quantity":False,
                "source":"{\"refer_urls\":[]}",
                "client_source":1,
                "shopid":int(ids), #dapet dari item model
                "itemid":int(idi), #dapet dari split product
                # "add_on_deal_id":int(idm) #dapet dari split product
                "modelid":int(idm)
                }
            else:
                payload1 = {
                "quantity":1,
                "checkout":True,
                "update_checkout_only":False,
                "donot_add_quantity":False,
                "source":"{\"refer_urls\":[]}",
                "client_source":1,
                "shopid":int(ids), #dapet dari item model
                "itemid":int(idi), #dapet dari split product
                "add_on_deal_id":int(idm) #dapet dari split product
                # "modelid":int(idm)
                }
            while 1:
                response = self.r.post('https://shopee.co.id/api/v2/cart/add_to_cart', data=json.dumps(payload1))
                # print(payload1)
                print(response)
                print(response.content)
                add = response.json()
                status = add['error']
                if status == None:
                    print('Berhasil Add')
                    break
                else:
                    print('Gagal Add, Lets Loop')
                # if status == None:
                #     print('Berhasil Add')
                # else:
                #     print('Gagal Add, Lets Loop')
                #     break
                time.sleep(1)
        #     sp_header = {'referer': 'https://shopee.co.id/',
        #                 'content-type': 'application/json',
        #                 'x-csrftoken' : token_csrf,
        #                 'x-requested-with':'XMLHttpRequest',
        #                 'x-shopee-language':'id'}
        #     self.r.headers.update(sp_header)
        #     payload1 = {
        # "selected_shop_order_ids":[{"shopid":34547329,"item_briefs":[{"itemid":6246440761,"modelid":70599418763,"item_group_id":"null","applied_promotion_id":2006215377,"offerid":"null","price":5500000000,"quantity":1,"is_add_on_sub_item":"null","add_on_deal_id":"null","status":1,"cart_item_change_time":1606808363}],"shop_vouchers":[]}],"platform_vouchers":[]
        #     }
        #     response = self.r.post('https://shopee.co.id/api/v4/cart/checkout', data=json.dumps(payload1))
        #     print(payload1)
        #     print(response)
        #     print(response.content)

    # <<<<<<<<<<<<<< End Add To Cart Code >>>>>>>>>>>>>>>>

        def run(self):
            self.parse()
            time.sleep(0.3)
            self.get_model()
            time.sleep(0.2)
            print("Check Login Info..")
            # <<<<<<<<<<<<<< Check Login Info Code >>>>>>>>>>>>>>>>
            r = requests.Session()
            call_user = r.request("get","https://shopee.co.id/api/v2/user/profile/get/")
            user = call_user.json()
            status = user['error']
            print(status)
            print(call_user.status_code)
            if status == None:
                print('Check Login Info finish without error..')
                print('Sucessful Login')
            else:
                self.Login()
                time.sleep(0.2)
                self.add()
            # self.cek()
            print('\007')

if __name__ == '__main__':
    d = gas()
    d.run()
