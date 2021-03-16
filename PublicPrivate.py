prime1 = 37
prime2 = 43
prime3 = 19

publicKey = (prime1*prime2, prime3)
print("Your public key:", publicKey)

phi1 = prime1 - 1
phi2 = prime2 - 1

for d in range(1, phi1*phi2):
    if (d * prime3) % (phi1 * phi2) == 1:
        privateKey = (prime1*prime2, d)
        break
print("Your private key is (keep it secret!!!!!):", privateKey)


#Encryption

def encrypt(message,pkey):
    return (message**pkey[1])%pkey[0]

testmessage = input()
destkey = (2257,53)
outstr = ""
for eachletter in testmessage:
    outstr += str(encrypt(ord(eachletter),destkey)) + " "
print(outstr)
#Computer science is no more about computers than astronomy is about telescopes.
