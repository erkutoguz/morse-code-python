from playsound import playsound
import time

morse_code = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
              'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
              'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
              'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
              'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
              'Z': '--..', '0': '-----', '1': '.----', '2': '..---',
              '3': '...--', '4': '....-', '5': '.....', '6': '-....',
              '7': '--...', '8': '---..', '9': '----.', '.': '.-.-.',
              ',': '--..-', '?': '..--.'}


def encrypt(s: str):
    encrypted_text = []
    # l for letter
    for l in s:
        try:
            if l == ' ':
                encrypted_text.append(' ')
            elif l == 'i':
                encrypted_text.append(morse_code['I'])
            else:
                encrypted_text.append(morse_code[l.upper()])
        except KeyError as e:
            encrypted_text.append('X')

    return '/'.join(encrypted_text)


def decrypt(s: str):
    decrypted_text = []
    # c for char
    for c in s.split('/'):
        for k, v in morse_code.items():
            if v == c:
                decrypted_text.append(k)
        if c == ' ':
            decrypted_text.append(' ')

    return ''.join(decrypted_text)


def beep(code):
    # w for word
    for w in code.split('/'):
        if w != ' ':
            for c in w:
                if c == '.':
                    playsound('period.ogg')
                else:
                    playsound('dash.ogg')
        time.sleep(1)


# beep('./.-./-.-/..-/-/ /.--')
while True:
    cmd = input(
        "Type 'e' for encrypt, type 'd' for decrypt, type 'wq:' for exit: ")

    if cmd == 'e':
        text = input('Enter your message: ')
        output = encrypt(text)
        print(output)
        beep_cmd = input("Type 'y' for code sound, type 'n' for continue: ")
        if beep_cmd == 'y':
            beep(output)
        elif beep_cmd == 'n':
            pass
        else:
            print('Invalid command.')

    elif cmd == 'd':
        text = input('Enter your code, split with \'/\': ')
        output = decrypt(text)
        print(output)

    elif cmd == 'wq:':
        print('Thank you. GoodBye')
        break
    else:
        print('Invalid command. Try Again.')
