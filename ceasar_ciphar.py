# duplicate the alphabet to loop again from zero if in case the letter is z
print(''',adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
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
              88                                                                                                  ''')


# Combinig the two functions to create a single function which encodes and decodes the text
def ceasar(start_text,shift_amount,ciphar_direction):
    end_text=""
    if ciphar_direction == "decode":
            shift_amount *= -1
    for char in start_text:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = position+shift_amount
            end_text += alphabet[new_position]
        else:
             end_text += char    
    print(f"The {ciphar_direction }d text is :  {end_text}.") 

should_contine=True
while should_contine:
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    direction = input("Type 'encode' to encrypt and 'decode' to decrypt.\n")
    text = input("Type your message:  \n").lower()
    shift = int(input("Type the shift number: \n"))
    shift = shift% 26
    ceasar(start_text=text,shift_amount=shift,ciphar_direction=direction)

    result = input("Type 'yes' to continue , Type 'no' to end \n").lower()
    if result == "no":
         should_contine = False
         print("Goodbye!")





    

     




           

