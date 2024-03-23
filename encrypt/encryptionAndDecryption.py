#encrypted password will be saved as password in data base
#python file with encrypt and decrypt

from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

#encrypt data
#pass the data you want to encrypt and the key, retrun the ciphertext, tag, and nonce
def encrypt(data, key):
    cipher = AES.new(key, AES.MODE_EAX)
    ciphertext, tag = cipher.encrypt_and_digest(data)
    nonce = cipher.nonce
    encryptReturn = {'ciphertext': ciphertext, 'tag' : tag, 'nonce' : nonce}
    return encryptReturn
#decrypt data
#pass the data you want to decrypt, return the decrypted ciphertext (plaintext), the tag, and the nonce
def decrypt(key, ciphertext, tag, nonce):
    cipher = AES.new(key, AES.MODE_EAX, nonce)
    data = cipher.decrypt_and_verify(ciphertext, tag)
    decryptReturned =  {'data': data, 'tag' : tag, 'nonce' : nonce}
    return decryptReturned

data = b'secret data' 
key = get_random_bytes(16) #generate key
print("key: "+key.hex().upper())

encryptReturn = encrypt(data, key)
tagReturnedE = encryptReturn.get('tag') #tag returned from encryption 
cipherReturnedE = encryptReturn.get('ciphertext') #ciphertext returned from encryption 
nonceReturnedE = encryptReturn.get('nonce') #nonce returned from encryption 

print("ciphertext from encrypt: "+cipherReturnedE.hex().upper()) 
print("tag from encrypt: "+tagReturnedE.hex().upper())
print("tag from nonce: "+nonceReturnedE.hex().upper())

decryptReturned = decrypt(key, cipherReturnedE, tagReturnedE, nonceReturnedE)
plainTextReturnedD = decryptReturned.get('data') #plaintext returned from decryption 
tagReturnedD = decryptReturned.get('tag') #tag returned from decryption
nonceReturnedD = decryptReturned.get('nonce') #nonce returned from decryption

print("plaintext from decrypt: ", end = "")
print(plainTextReturnedD)
print("tag from decrypt: "+tagReturnedD.hex().upper())
print("nonce from decrypt: "+nonceReturnedD.hex().upper())

#need plaintext, ciphertext, nonce, tag, key
#each user a their own key, the nonce and the tage are generate indvidually for each a password 