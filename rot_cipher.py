letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def rot():
    endecrypt = input("Would you like to encrypt or decrypt?\n")
    while endecrypt != "encrypt" and endecrypt != "decrypt":
        print("Please enter encrypt or decrypt")
        endecrypt = input()
    
    print("How many rotations?")
    while True:
        try:
            rotations = int(input())
            if 0 <= rotations <= 26:
                break
        except ValueError:
            print("Please enter a number 0-26")

    text = input("What would you like to encode?\n")
    
    encoded = ''
    for char in text:
        upper = False
        if char.isupper():
                upper = True
                char = char.lower()

        if char not in letters:
            encodedchar = char
        
        else:
            charindex = letters.index(char)
            
            if endecrypt == "encrypt":
                encodedchar = letters[charindex + rotations]

            if endecrypt == "decrypt":
                encodedchar = letters[charindex - rotations]
            
            if upper:
                encodedchar = encodedchar.upper()

        encoded = encoded + encodedchar
        
    print(encoded)

rot()