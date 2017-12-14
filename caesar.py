def alphabet_position(letter):
    return ord(letter.lower()) - 97

def rotate_character(char, rot):
    if not char.isalpha():
        return char
    if char.isupper():
        new_ord = alphabet_position(char) + rot 
        new_ord = new_ord % 26 + 97
        new_char = chr(new_ord)
        new_char = new_char.upper()
    else:    
        new_ord = alphabet_position(char) + rot 
        new_ord = new_ord % 26 + 97        
        new_char = chr(new_ord)
        return new_char
    
def encrypt(text, rot):
    encrypted = str("")
    for letter in text:
        encrypted += str(rotate_character(letter, rot))
    return encrypted

print(encrypt("abcd" , 13 ))