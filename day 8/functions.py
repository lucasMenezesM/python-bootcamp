# import alphabetData

def greet(name):
    print(f"Hello {name}")


def greet_with(name, location):
    print(f"Hello, {name}. You are from {location}, right?")


def calc_paint(width, height, coverage):
    result = (width * height) / coverage
    return round(result, 0)


def prime_number(n):
    prime_number = True

    for i in range(2, n):
        if n % i == 0:
            prime_number = False
    if prime_number and n != 1:
        return f"{n} is a prime number"
    else:
        return f"{n} is not a prime number"


# def encrypt(text, shift):
#     encrypted_list = []
#     new_range = []

#     for i in range(shift, len(alphabet)):
#         encrypted_list.append(alphabet[i])

#     for i in range(0, shift):
#         encrypted_list.append(alphabet[i])

#     for i in range(len(text)):
#         new_range.append(alphabet.index(text[i]))
#     encrypted_word = ""
#     for i in range(len(new_range)):
#         encrypted_word += encrypted_list[new_range[i]]
#     print(f"The encoded text is {encrypted_word}")
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def encrypt(text, shift):
    encrypted_word = ""

    for letter in text:
        position = alphabet.index(letter)
        new_position = position + 5
        encrypted_word += alphabet[new_position]

    print(f"The encrypted word is {encrypted_word}")


def decrypt(text, shift):
    decrypted_word = ""

    for letter in text:
        position = alphabet.index(letter)
        new_position = position - shift
        decrypted_word += alphabet[new_position]

    print(f"The decrypted word is {decrypted_word}")


def caeser(text, shift, direction):
    new_word = ""

    if shift > 26:

        shift = shift % 26

    if direction == "decode":
        shift *= -1

    for letter in text:

        if letter not in alphabet:
            new_word += letter
            continue

        position = alphabet.index(letter)

        new_position = position + shift

        new_word += alphabet[new_position]

    print(f"The {direction}d is {new_word}")
