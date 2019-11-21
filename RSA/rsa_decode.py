# 常规RSA解密
import gmpy2

p = gmpy2.mpz(1108609086364627583447802163)
q = gmpy2.mpz(782758164865345954251810941)
#k = gmpy2.mpz(1108609086364627583447802163)

e = gmpy2.mpz(59159)
phi_n = (p - 1)
d = gmpy2.invert(e, phi_n)
print ("private key:")
print (d)

c = gmpy2.mpz(449590107303744450592771521828486744432324538211104865947743276969382998354463377)

# 读取flag.enc
# with open('flag.enc', 'r') as f:
#     c = f.read().encode('hex')
#     c = int(c, 16)

print("plaintext:")
M  =  pow(c,d,p*q)
print('[10进制]' + str(M))
flag = str(hex(M))[2:]
print('[16进制]' + flag)
print('[ASCII码]' + bytes.fromhex(flag).decode('utf-8'))