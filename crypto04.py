import gmpy2

x = pow(2,166)+pow(2,154)+pow(2,121)+pow(2,82)+pow(2,71)+pow(2,43)+pow(2,12)+pow(2,1)
y = pow(2,166)+pow(2,151)+pow(2,111)+pow(2,72)+pow(2,66)+pow(2,55)+pow(2,22)+pow(2,1)

p = gmpy2.next_prime(x**3 + y**3)
q = gmpy2.next_prime(x**2*y + y**2*x)

e = gmpy2.mpz(65537)
phi_n = (p - 1) * (q - 1)
d = gmpy2.invert(e, phi_n)
print ("private key:")
print (d)

c = gmpy2.mpz(2572184203530319119243802092734267367739314260153168372813084861532107980149141078303814618325602324697946352068777451604814640830191963407865014196272283999887850489256809511239366180658226561342463921245368725238264825962755084034124440395640873055757249835228336127259905690718814413104196580700746)


print("plaintext:")
M  =  pow(c,d,p*q)
print('[10进制]' + str(M))
flag = str(hex(M))[2:]
print('[16进制]' + flag)
print('[ASCII码]' + bytes.fromhex(flag).decode('utf-8'))