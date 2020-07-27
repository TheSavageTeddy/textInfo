import base64
import codecs
import binascii
from requests.utils import requote_uri
from urllib.parse import unquote

text=input("Enter text: ")
print("Text length:", len(text))
print('''
-------------------------------
            Base 64
-------------------------------
''')
print("Base64 decode (if any): ", base64.decode(text))
print("Base64 encode (if any): ", base64.encode(text))
print('''
-------------------------------
            Base 32
-------------------------------
''')
print("Base32 decode (if any): ", base32.decode(text))
print("Base32 encode (if any): ", base32.encode(text))
