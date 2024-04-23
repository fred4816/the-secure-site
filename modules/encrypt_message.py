from cryptography.fernet import Fernet


def encrypt_text(text_to_encrypt):
    key = Fernet.generate_key()
    
    with open('../temp/decryptkey.txt', 'wb') as decrypt_key_file:
        decrypt_key_file.write(key)
    
    encrypt_class = Fernet(key)

    token = encrypt_class.encrypt(text_to_encrypt)

    with open('../temp/encrypt.txt', 'wb') as encrypt_file:
        encrypt_file.write(token)


def decrypt_text():
    with open('../temp/decryptkey.txt', 'r') as decrypt_key_file:
        decrypt_class = Fernet(decrypt_key_file.read())
    
    with open('../temp/encrypt.txt', 'r') as encrypted_file:
        print(decrypt_class.decrypt(encrypted_file.read()).decode('utf-8'))


def main():
    text_to_encrypt = bytes(input('Enter the text you would like to encrypt: '), 'utf-8')
    encrypt_text(text_to_encrypt)
    # encrypt_text()
    decrypt_text()

main()