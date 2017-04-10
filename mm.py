# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
from Crypto.Cipher import AES 
import importlib,sys
importlib.reload(sys)


s = requests.session()
linfo  = s.get('http://192.168.0.1/login_pc.htm',headers={'Referer':'http://192.168.0.1/login.htm'})
#d = {'user':'admin','pass': '4f111c8fc15a6aa538bd23012af17a7'}
rkey = s.get('http://192.168.0.1/router/get_rand_key.cgi')
dic = eval(rkey.text)

iv = "360luyou@install"
key = dic['rand_key'][32:64]
key_index = dic['rand_key'][0:32]

data = "PDPpdp054303132"
bs = AES.block_size
padding = bs - len(data) % bs
padding_text = chr(padding) * padding
data = data + padding_text
generator  = AES.new(key, AES.MODE_CBC, iv)
ciphertext = generator.encrypt(data)

#msg = iv + cipher.encrypt(b'Attack at dawn')

print(ciphertext.decode('utf8'))
