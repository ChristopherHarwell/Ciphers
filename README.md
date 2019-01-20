# Ciphers
XOR DECRYPTION AND ENCRYPTION
#-------------------------------------------------------------------------------
# Name:        XOR CIPHER
# Purpose:     XOR message Encryption and Decryption
#
# Author:      Christopher Harwell
#
# Created:     20/01/2019
# Copyright:   (c) SpaceCaseCoder,Inc. 2019
# Licence:     <SpaceCaseCoder,Inc.>
#-------------------------------------------------------------------------------

def cipher_encryption():
    message = input("Enter message: ")
    key = input(("Enter key: "))

    encrypt_hex = ""
    key_itr = 0
    for i in range(len(message)):
        temp = ord(message[i]) ^ ord(key[key_itr])
        encrypt_hex += 1
        if key_itr >= len(key):
            key_itr = 0
    print("Encrypted Text: {}".format(encrypt_hex))


def cipher_decryption():
    message = input("Enter Message: ")
    key = input("Enter Key: ")


    hex_to_uni = ""
    for i in range(0,len(message), 2):
        hex_to_uni += bytes.fromhex(message[i : i + 2]).decode("utf-8")
    decrypt_text = ""
    key_itr = 0
    for i in range(len(hex_to_uni)):
        temp = ord(hex_to_uni[i]) ^ ord(key[key_itr])
        decrypt_text += chr(temp)
        key_itr += 1
        if key_itr >= len(key):
            key_itr = 0
    print("Decrypted Message: {}".format(decrypt_text))


def main():
    choice = int(input("\t1.Encryption\n\t2.Decryption\n\tChoose(1,2): "))
    if choice == 1:
        print("---Encryption---")
        cipher_encryption()
    elif choice == 2:
        print("---Decryption---")
        cipher_decryption()
    else:
        print("Invalid Choice!\n Please Pick Option 1 or 2, to continue.")
if __name__ == "__Main__":
    main()
