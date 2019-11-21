import xxtea
import binascii
text = "1111111111111111111"
key = "flag"
#encrypt_data = xxtea.encrypt(text, key)

encrypt_data = binascii.a2b_hex(b'bca5ce40f4b2b2e7a9129d12ae10c85b3dd7061ddc70f8dc')
decrypt_data = xxtea.decrypt(encrypt_data, key)
print(decrypt_data)