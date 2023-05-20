import hashlib


def password_encryption(plaintext):
    ciphertext = hashlib.md5(plaintext.encode())
    print("========================ENCRYPETDSUCCESSFULLY=======================")
    print(ciphertext.hexdigest())                                                                                                                                                                                                                                                                                                                                                                                                     

password_encryption(input("Enter Plaintext: "))      

# Steganography: technique of hidding information(text,malwares,spyware) on images

# Binwalk: Computer Forensic to analyse and extract information hidden images