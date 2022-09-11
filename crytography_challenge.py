#Cryptography Challenge #1 - www.101computing.net/cryptography-challenge-1/
import random, time

#A basic encryption algorithm...
def encrypt(plaintext, key):
  alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
  ciphertext = ""
  for i in range(0,len(plaintext)):
    character = plaintext[i]
    ciphertext = ciphertext + character
    for j in range (0,key):
      ciphertext = ciphertext + random.choice(alphabet)
  return ciphertext

#A basic decrytion algorithm...
def decrypt(cyphertext, key):
    return cyphertext[::key+1]

#Main program starts here...
#Input...
cyphertext = input("Enter a message to encrypt (cyphertext)")
key = int(input("Input a key as a number between 1 and 10"))
while not (key>=1 and key<=10):
  print("Invalid key, try again!")
  key = int(input("Input a key as a number between 1 and 10"))

#Process...  
print("...")
time.sleep(1)
print("Encrypting plaintext...")
time.sleep(1)
print("...")
time.sleep(1)
plaintext = decrypt(cyphertext, key)

#Output...
print("Ciphertext:")
print(ciphertext)
print("Plaintext:")
print(plaintext)