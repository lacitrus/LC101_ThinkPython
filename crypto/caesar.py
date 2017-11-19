def alphabet_position(letter):
    
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    alphabet2 = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    if letter in alphabet:
        for i in range(len(alphabet)):
            if letter == alphabet[i]:
                return i
    else:
        for i in range(len(alphabet2)):
            if letter == alphabet2[i]:
                return i

def rotate_character(char, rot):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    alphabet2 = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    
    if char in alphabet:
        index = (alphabet_position(char) + rot ) % 26
        return alphabet[index]
    elif char in alphabet2:
        index2 = (alphabet_position(char) + rot ) % 26
        return alphabet2[index2]
    else:
        return char

def encrypt(text, rot):
    newtext = ''
    for char in text:
        newtext += rotate_character(char, rot)
    return newtext

def main():
    message = input("Type a message:")
    rotate_number = int(input("Rotate by:"))
    print(encrypt(message, rotate_number))

if __name__ == "__main__":
    main()