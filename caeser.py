def encrypt(string,shift):

    cipher = ''
    for char in string:
        if char == '':
            cipher = cipher + char

        elif char.isupper():
            cipher = cipher + chr((ord(char)+ shift - 65)%26 +65)

        else:
            cipher = cipher + chr((ord(char)+ shift - 97)%26 +97)

    return cipher

text = input("Enter Message: ")
s = 3
print ("Original Message :",text)
print ("After encryption :",encrypt(text, s))
