import socket
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad,unpad
from Crypto.Random import get_random_bytes
from Crypto.Hash import HMAC, SHA512
import time

server_ip='127.0.0.1'
server_port =1234
key=b'+\x01\xfd\x89\x12\x15E\xceah\xe9^J\\\xa9['
iv=b'\xd4/\x03\x8br\xc2d\xb3\x1fg\x05]\xd2h\xb5k'
HMAC_KEY= b'\x9a$o\xad\xa4\xd18\xeb\x8c\xd74N\xda\xc5\x80\x95'

def hmac(message):
    obj=HMAC.new(HMAC_KEY,digestmod=SHA512)
    obj.update(message.encode('utf-8'))
    global digest
    digest=obj.digest()
    

def decryption(res):
    cipher=AES.new(key,AES.MODE_CBC,iv=iv)
    bytes_data=unpad(cipher.decrypt(res),AES.block_size)
    global decrypted_data
    decrypted_data=bytes_data.decode('utf-8')


def encryption(msg):
    msg=msg.encode('utf-8')
    cipher=AES.new(key,AES.MODE_CBC,iv)
    global encrypted_data
    encrypted_data=cipher.encrypt(pad(msg,AES.block_size))


def run_client():
    
    client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    try:
        client.connect((server_ip,server_port))
        while True:
            msg=input('Client :')
            
            if msg:
                hmac(msg)
                encryption(msg)

            client.send(encrypted_data[:1024])
            time.sleep(0.25)
            client.send(digest[:1024])
            response=client.recv(1024)
            response1=client.recv(1024)
            if response:
                decryption(response)
                hmac(decrypted_data)
            if digest != response1:
                print('The message is corrupted')
            
            if decrypted_data.lower()=='closed':
                break
            print(f'Server : {decrypted_data}')
        client.close()
        print('Connection to server closed')
    except Exception as e:
        print(e)

run_client()