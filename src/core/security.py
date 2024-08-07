from cryptography.fernet import Fernet

def encrypt_data(data):
    key = Fernet.generate_key()
    f = Fernet(key)
    return f.encrypt(data.encode()), key

def decrypt_data(encrypted_data, key):
    f = Fernet(key)
    return f.decrypt(encrypted_data).decode()

# Note: In a real application, you'd need to securely store and manage the encryption keys
