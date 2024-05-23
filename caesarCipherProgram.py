
#Exercise 1: 
#define alphabit 
def getDoubleAlphabet(alphabet):
    doubleAlphabet = alphabet + alphabet
    return doubleAlphabet
#######################################################


#Prova fucnion  con string
#alphabet="ABC"
#print(getDoubleAlphabet(alphabet))


#########################################################

#Creating Encrypting a message.
#function returns a string, it doesn’t take an argument to return the the input message.

def getMessage(): 
 #Get the message from the user
 stringToEncrypt = input("Please enter a message to encrypt: ")
#return the value of the varible stringToEncrypt.
 return stringToEncrypt



#########################################################
#Exercise 3: Getting a cipher key

def getCipherKey():
    
    shiftAmout= input("Please enter a key (Whole number from 1 to 25): ")
    return shiftAmout


#########################################################
#Exercise 4: Encrypting a message

def encryptMessage(message,cipherKey, alphabet):
    encryptedMessage = ""
    uppercaseMessage = ""

    #print(uppercaseMessage)
    uppercaseMessage= message.upper()
    
    #for loop to shift each letter in the message
    for currentCharcter in uppercaseMessage:
       position = alphabet.find(currentCharcter)
       newPosition = (position + int(cipherKey))
       if currentCharcter in alphabet:
          #if the corrent caracter is exist then add it to the encrypted message.if not then add it to the encrypted message.
          encryptedMessage = encryptedMessage + alphabet[newPosition]
       else:
          encryptedMessage += currentCharcter

    return encryptedMessage

#########################################################

##Exercise 5: Decrypting a message
#function by reusing the encryptMessage() function

def decryptMessage(message,cipherKey, alphabet):
   
   #shifting each letter back
   descryptKey= -1 * int(cipherKey)

   return encryptMessage(message,descryptKey, alphabet) 


#########################################################

#Exercise 6: Creating a main function
#built a collection of user-defined functions that will help you write a Caesar cipher program. Define a string var""" iable to contain the English alphabet.

""" To be able to shift letters, double your alphabet string.

Get a message to encrypt from the user.

Get a cipher key from the user.

Encrypt the message.

Decrypt the message. """

def runCaesarCipherProgram():
    myAlphabet="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    print(f'Alphabet: {myAlphabet}')
    myAlphabet2 = getDoubleAlphabet(myAlphabet)
    print(f'Alphabet2: {myAlphabet2}')
  
    #variable to store the functions to print it 
    myMessage = getMessage()
    print(myMessage)
    myCipherKey = getCipherKey()
    print(myCipherKey)
  
    #variables to store the functions  .
    myEncryptedMessage = encryptMessage(myMessage, myCipherKey, myAlphabet2)
    # 
    print(f'Encrypted Message: {myEncryptedMessage}')
    myDecryptedMessage = decryptMessage(myEncryptedMessage, myCipherKey, myAlphabet2)
    print(f'Decypted Message: {myDecryptedMessage}')
    
runCaesarCipherProgram()