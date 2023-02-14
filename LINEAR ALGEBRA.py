import numpy as np

privateKeyMatrix = [[2,1],[34,12]] # private key and it will be edited as we want it to be
messageCodes = {' ': 0,
                'a': 1,'b': 2,'c': 3,'d': 4,'e': 5,'f': 6,'g': 7, 'h': 8,'i': 9,'j': 10,'k': 11,'l': 12, 'm': 13,'n': 14,'o': 15,'p': 16,'q': 17, 'r': 18,'s': 19, 't': 20, 'u': 21, 'v': 22, 'w': 23,'x': 24,'y': 25,'z': 26,
                '0': 27,'1': 28,'2': 29,'3': 30,'4': 31,'5': 32,'6': 33,'7': 34,'8': 35,'9': 36,
                'A':37,'B':38, 'C':39, 'D':40, 'E':41,'F':42,'G':43,'H':44,'I':45,'J':46,'K':47,'L':48,'M':49,'N':50,'O':51,'P':52,'Q':53,'R':54,'S':55,'T':56,'U':57,'V':58, 'W':59,'X':60,'Y':61, 'Z':62
}

message = str(input("\n\nEnter your text : \n"))

def getPublicKeyMatrix():
    # a function to convert the public key from user to a matrix 2x2
    publicKeyMatrix:list = [[],[]]
    publicKey = str(input("\nEnter your public key : \n"))
    if (len(message) % 2 == 1):
        publicKey = publicKey+" "
    for i in range(len(publicKey)//2):
        publicKeyMatrix[0].append(messageCodes[publicKey[i]])

    for i in range(len(publicKey)//2, len(publicKey)):
        publicKeyMatrix[1].append(messageCodes[publicKey[i]])
    
    if len(publicKeyMatrix[0]) > 2: # to decrese the size of nx2 matrix to a 2x2 matrix
        publicKeyMatrix[0] = [sum(publicKeyMatrix[0][0:len(publicKeyMatrix[0])//2]), sum(publicKeyMatrix[0][len(publicKeyMatrix[0])//2:len(publicKeyMatrix[0])])]
        publicKeyMatrix[1] = [sum(publicKeyMatrix[1][0:len(publicKeyMatrix[1])//2]), sum(publicKeyMatrix[1][len(publicKeyMatrix[1])//2:len(publicKeyMatrix[1])])]

    return publicKeyMatrix

publicKeyMatrix = getPublicKeyMatrix() # size = 2x2

def encryption(message:str, key:list):
    messageMatrix = [[], []]
    encryptedMatrix = [[], []]
    key = np.matmul(np.array(publicKeyMatrix), np.array(key))

    if (len(message) % 2 == 1):
        message = message+" "
    
    for i in range(len(message)//2):
        messageMatrix[0].append(messageCodes[message[i]])
    for i in range(len(message)//2, len(message)):
        messageMatrix[1].append(messageCodes[message[i]])

    # multiplication of two matrices
    for i in range(len(messageMatrix[0])):
        encryptedMatrix[0].append((key[0][0] * messageMatrix[0][i]) + (key[0][1] * messageMatrix[1][i]))
    for i in range(len(messageMatrix[0])):
        encryptedMatrix[1].append((key[1][0] * messageMatrix[0][i]) + (key[1][1] * messageMatrix[1][i]))

    # getting the letters from messageCodes dictionary 
    print("\nEncrypted text is: ")
    for i in range(len(encryptedMatrix[0])):
        print(chr(encryptedMatrix[0][i]), end="")
    for i in range(len(encryptedMatrix[1])):
        print(chr(encryptedMatrix[1][i]), end="")

    return encryptedMatrix


def decryption(key:list, encrypted:list):
    inverseKey = [[], []]
    decryptedMatrix = [[], []]
    key = np.matmul(np.array(publicKeyMatrix), np.array(key))


    inverseKey[0].append(key[1][1])
    inverseKey[0].append(key[0][1] * -1)
    inverseKey[1].append(key[1][0] * -1)
    inverseKey[1].append(key[0][0])

    for i in range(2):
        for j in range(2):
            try:
                inverseKey[i][j] = inverseKey[i][j] * (1/((key[0][0]*key[1][1]) - (key[0][1]*key[1][0])))
            except:
                inverseKey[i][j] = 0
    for i in range(len(encrypted[0])):
        decryptedMatrix[0].append(round((inverseKey[0][0] * encrypted[0][i]) + (inverseKey[0][1] * encrypted[1][i])))
    for i in range(len(encrypted[0])):
        decryptedMatrix[1].append(round((inverseKey[1][0] * encrypted[0][i]) + (inverseKey[1][1] * encrypted[1][i])))

    print("Decrypted text is: ")
    for i in range(len(decryptedMatrix[0])):
        value = list(messageCodes.keys())
        print(value[decryptedMatrix[0][i]], end="")
    for i in range(len(decryptedMatrix[1])):
        value = list(messageCodes.keys())
        print(value[decryptedMatrix[1][i]], end="")

    print("\n\n")
    return decryptedMatrix

m = encryption(message, publicKeyMatrix)
print("\n")
decryption(publicKeyMatrix, m)
