import art
print(art.shape)
alphabets=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
# def encrypt(original_text,shift_number):
#     cipher_text=""
#     for letter in original_text:
#         shifted_position=(alphabets.index(letter)+shift_number)%26
#         cipher_text+=alphabets[shifted_position]
#     print(f"here is the encoded text: {cipher_text}")

# def decrypt(original_text,shift_number):
#     plain_text=""
#     for letter in original_text:
#         shifted_position=(alphabets.index(letter)-shift_number)%26
#         plain_text+=alphabets[shifted_position]

#     print(f"here is the decoded text: {plain_text}")    
# if direction=="encode":
#        encrypt(original_text=text,shift_number=shift)
# elif direction=="decode":
#      decrypt(original_text=text,shift_number=shift) 

def ceasar(original_text,shift_number,encode_or_decode):
    output_text=""
    if encode_or_decode=="decode":
            shift_number*=-1
    for letter in original_text:
        if letter not in alphabets:
            output_text+=letter
        else:
            shifted_position=(alphabets.index(letter)+shift_number)%26
            output_text+=alphabets[shifted_position]
    print(f"here is the {encode_or_decode}d text: {output_text}")

should_continue=True
while should_continue:
    direction=input("Type 'encode' to encrypt, Type 'decode' to decrypt:\n ")
    text=input("Type your message:\n").lower()
    shift=int(input("enter the shift number:\n"))
    ceasar(original_text=text,shift_number=shift,encode_or_decode=direction)
    restart=input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
    if restart=="no":
        should_continue=False
        print("Goodbye")
