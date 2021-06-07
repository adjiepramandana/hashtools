from art import *
from simhash import *
import sys
import zlib
import base64
import hashlib
import time

def toolbase64_decode():
    base64_message = input("Insert Base64 Encode :")
    base64_bytes = base64_message.encode('ascii')
    message_bytes = base64.b64decode(base64_bytes)
    message = message_bytes.decode('ascii')
    time.sleep(2)
    print("Reading........")
    time.sleep(2)
    print("Enchanching......")
    time.sleep(2)
    print("Decode Procces.....")
    time.sleep(1)
    print("Success Your String is :",message)
    
def toolbase64_encode():
    message = input("Insert Your Text :")
    message_bytes = message.encode('ascii')
    base64_bytes = base64.b64encode(message_bytes)
    base64_message = base64_bytes.decode('ascii')
    time.sleep(2)
    print("Reading........")
    time.sleep(2)
    print("Enchanching......")
    time.sleep(2)
    print("Encode Procces.....")
    time.sleep(1)
    print("Success Your Base64 is :",base64_message)
    
    
def toolmd5_encode():
    getdata_encmd5 = input("Insert Your Text :")
    hasil_encmd5 = hashlib.md5(getdata_encmd5.encode('utf-8')).hexdigest()
    time.sleep(2)
    print("Reading........")
    time.sleep(2)
    print("Enchanching......")
    time.sleep(2)
    print("Encode Procces.....")
    time.sleep(1)
    print("Success Your md5 is :",hasil_encmd5)
    

def toolmd5_dec():
    print("For md5 Decrypt Visit This Site : https://www.md5online.org/")
    

def toolzlib_enc():
    getdata_enczlib = input("Insert Your Text :")
    hasil_enczlib = zlib.adler32(getdata_enczlib.encode('utf-8')) & 0xffffffff
    time.sleep(2)
    print("Reading........")
    time.sleep(2)
    print("Enchanching......")
    time.sleep(2)
    print("Encode Procces.....")
    time.sleep(1)
    print("Success Your zlib is :",hasil_enczlib)
    

def toolsha256_encode():
    getdata_encsha256 = input("Insert Your Text :")
    hasil_encsha256 = hashlib.sha256(getdata_encsha256.encode('utf-8')).hexdigest()
    time.sleep(2)
    print("Reading........")
    time.sleep(2)
    print("Enchanching......")
    time.sleep(2)
    print("Encode Procces.....")
    time.sleep(1)
    print("Success Your sha256 is :",hasil_encsha256)
    
    

    
def toolsimhash_encode():
    getdata_encsimhash = input("Insert Your Text :")
    hasil_encsimhash = Simhash(getdata_encsimhash).value
    time.sleep(2)
    print("Reading........")
    time.sleep(2)
    print("Enchanching......")
    time.sleep(2)
    print("Encode Procces.....")
    time.sleep(1)
    print("Success Your simhash is :",hasil_encsimhash)
    
    
def toolsha1_encode():
    getdata_encsha1 = input("Insert Your Text :")
    hasil_encsha1 = hashlib.sha1(getdata_encsha1.encode('utf-8')).hexdigest()
    time.sleep(2)
    print("Reading........")
    time.sleep(2)
    print("Enchanching......")
    time.sleep(2)
    print("Encode Procces.....")
    time.sleep(1)
    print("Success Your sha1 is :",hasil_encsha1)
    
    
Art = text2art("Hash-Tools", font='big', chr_ignore=True)

print(Art)


print("============================= Hash-Tool V1 =================================== \n                          Made By Jie With ❤ \n     ============================= ++ ===================================")
time.sleep(1)

get_user = input("Chose Menu : \n [1]Base64 Encode \n [2]Base64 Decode \n [3]md5 Encode \n [4]md5 Decode \n [5]Zlib Encode \n [6]Simhash Encode \n [7]SHA256 Encode \n [8]SHA1 Encode \n [9]About Developers \n [10]Exit \n \n :")
        

if (get_user == "1"):
    toolbase64_encode()
elif (get_user == "2"):
    toolbase64_decode()
elif (get_user == "3"):
    toolmd5_encode()
elif (get_user == "4"):
    toolmd5_dec()
elif (get_user == "5"):
    toolzlib_enc()
elif (get_user == "6"):
    toolsimhash_encode()
elif (get_user == "7"):
    toolsha256_encode()
elif (get_user == "8"):
    toolsha1_encode()
elif (get_user == "9"):
    print(" \n -Adjie Pramandana \n -Alvaro Xavien")
elif (get_user == "10"):
    print("Thanks For Use This Tool")
    sys.exit()
else: 
    print(get_user)


