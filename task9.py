logo = """           
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88           
"""
def ceasar(original_txt,shifted_amount,enc_dec):
    output_tst=""
    if enc_dec == "decode":
        shifted_amount *= -1

    for letter in original_txt:

        if letter not in alphabet:
            output_tst+=(letter)
        else:
            shifted_position=alphabet.index(letter)+shifted_amount
            shifted_position%=len(alphabet)
            output_tst+=alphabet[shifted_position]
    print(f"Here is the {enc_dec}d letters: {output_tst}")

caesar_continue=True
while caesar_continue:
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
                'v', 'w', 'x', 'y', 'z']
    direction = input("Type 'encode' to encode or 'decode' to decode: \n")
    text = input("Type Your Text: \n")
    shift = int(input("Type the shift want to change: \n"))

    ceasar(text,shift,direction)

    restart=input(f"Type yes to continue no to exit: ").lower()
    if restart=="no":
        caesar_continue=False
        print("Thank you for Playing!")





