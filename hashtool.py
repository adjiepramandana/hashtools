from art import *
import base64
import hashlib
import time

def toolbase64_decode():
    getdata_dec = input("Insert Base64 Encode :")
    hasil_dec = base64.b64decode(getdata_dec)
    time.sleep(2)
    print("Reading........")
    time.sleep(2)
    print("Enchanching......")
    time.sleep(2)
    print("Decode Procces.....")
    time.sleep(1)
    print("Success Your String is :",hasil_dec)
    
def toolbase64_encode():
    getdata_enc = input("Insert Your Text :")
    hasil_enc = base64.b64encode(getdata_enc)
    time.sleep(2)
    print("Reading........")
    time.sleep(2)
    print("Enchanching......")
    time.sleep(2)
    print("Encode Procces.....")
    time.sleep(1)
    print("Success Your Base64 is :",hasil_enc)
    
    
def toolmd5_encode():
    getdata_encmd5 = input("Insert Your Text :")
    hasil_encmd5 = hashlib.md5(getdata_encmd5)
    time.sleep(2)
    print("Reading........")
    time.sleep(2)
    print("Enchanching......")
    time.sleep(2)
    print("Encode Procces.....")
    time.sleep(1)
    print("Success Your md5 is :",hasil_encmd5)
    

def toolmd5_dec():
    print("SORRY MD5 DECRYPT IS COMING SOON:)")
    

Art = text2art("Hash-Tools", font='big', chr_ignore=True)

print(Art)


print("============================= Hash-Tool V1 =================================== \n                          Made By Jie With ❤ \n     ============================= ++ ===================================")
time.sleep(1)

get_user = input("Chose Menu : \n [1]Base64 Encode \n [2]Base64 Decode \n [3]md5 Encode \n [4]md5 Decode \n \n :")
        

if (get_user == "1"):
    toolbase64_encode()
elif (get_user == "2"):
    toolbase64_decode()
elif (get_user == "3"):
    toolmd5_encode()
elif (get_user == "4"):
    toolmd5_dec()
else:
    print(get_user)


