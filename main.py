from caesar_cipher_art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print(logo)

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n")) % 26

def caesar(direction_input, text_input, shift_input):
  if direction == "encode":
    encrypt_cipher_text = ""
    for letter in text_input:
      if letter in alphabet:
        encrypt_position = alphabet.index(letter)
        encrypt_new_position = encrypt_position + shift_input
        encrypt_new_letter = alphabet[encrypt_new_position]
        encrypt_cipher_text += encrypt_new_letter
      else:
        encrypt_cipher_text += letter
    print(f"The encoded text is {encrypt_cipher_text}")

  elif direction == "decode":
    decode_cipher_text = ""
    for letter in text_input:
      if letter in alphabet:
        decode_position = alphabet.index(letter)
        decode_new_position = decode_position - shift_input
        decode_new_letter = alphabet[decode_new_position]
        decode_cipher_text += decode_new_letter
      else:
        decode_cipher_text += letter
    print(f"The decoded text is {decode_cipher_text}")

  else:
    print("Invalid Input")

caesar(direction_input=direction, text_input=text, shift_input=shift)
