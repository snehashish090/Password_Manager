import string
def encrypt(text, key):

    encrypted_text = ""

    for i in text:

        try:
            encrypted_text += letters[(letters.index(i) + key) % len(letters)]

        except ValueError:
            encrypted_text += i

    return encrypted_text


def decrypt(text, key):

    decrypted_text = ""
    for i in text:
        try:
            decrypted_text += letters[letters.index(i) - key % len(letters)]
        except ValueError:
            decrypted_text += i
    return decrypted_text


letters = string.ascii_letters
