
morse_code_dict = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....', 'I': '..',
    'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
    'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..',
    '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...',
    '8': '---..', '9': '----.',
    ' ': ' '
}

def morse_to_english():
  user_input = input("Enter your morse code here : ").split('/')
  print(user_input)
  english_arr = []
  for char in user_input:
    for key,value in morse_code_dict.items():
      if value == char:
        english_arr.append(key)
  print(''.join(english_arr).title())


def english_to_morse():
  user_input = input('Enter your Text Here : ').upper()
  morse_arr = []
  for char in user_input:
    if char in morse_code_dict:
      morse_arr.append(morse_code_dict[char])
    else:
      pass
  print(''.join(morse_arr))

message = """
1 - translate from morse to english.
2 - translate from english to morse.
3 - Quite
"""

while True:
  print(message)
  choice = input('Enter your choice ? : ')
  if choice == '1':
    morse_to_english()
  elif choice == '2':
    english_to_morse()
  elif choice == '3':
    break
  else:
    print('Input is invalid please enter valid choice !!')
