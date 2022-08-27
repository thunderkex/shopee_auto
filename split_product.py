import re

regex = r"https://shopee\Wco.id/(.*?)-i.(?P<shop>\d+)\W(?P<item>\d+)"

test_str = "https://shopee.co.id/Samsung-Galaxy-A21s-6GB-128GB-Silver-Exclusive-Shopee-Free-Disney-Casing-i.52635036.7258395159"

for match in re.finditer(regex,test_str):
    iditem = match["item"]#Hasil Item ID
    idshop = match["shop"]#Hasil Shop ID
print(iditem)
print(idshop)