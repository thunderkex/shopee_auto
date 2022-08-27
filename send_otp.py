print('Trying with OTP Code')
cokee = {'cookie':"csrftoken=" + crsf_login + "; " + cookie_string2}
token_csrf = crsf_login
r.cookies.update(cokee)
print('Send OTP code To your whatsapp number')
url="https://shopee.co.id/api/v2/authentication/resend_otp"
response2 = r.request("POST",url,headers=headers, data = '{"operation":5,"channel":3,"support_whats_app":true,"force_channel":true}')
print(response2.status_code)
data = input("Please enter a Verif code: ")
url="https://shopee.co.id/api/v2/authentication/vcode_login"
response2 = r.request("POST",url,headers=headers, data = '{"email":"EMAIL MU","otp":"'+ data +'"}')
print(response2.status_code)
print('Lets Run')