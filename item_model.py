import requests
import json

r = requests.Session()
call_model = r.request("get","https://shopee.co.id/api/v2/item/get?itemid=4746602276&shopid=34547329")
model = call_model.json()
if 'model_id' in model['item']['models'][0]['price_stocks'][1]:
    print(model['item']['models'][0]['price_stocks'][1]['model_id'])
if 'flash_sale' in model['item']:
    print(model['item']['flash_sale']['promotionid'])
# if 'model_id' in model['item']:
#     print(model['model_id'])
# print(list(filter(lambda x:x["model_id"],model)))
# get = model['item']['models'][0]['price_stocks'][1]['model_id']
# print(get)#Hasil Model ID