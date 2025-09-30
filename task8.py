alphabet=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
direction=input("Type 'encode' to encode or 'decode' to decode: ")
text=input("Type your text:")
shift=int(input("Type your shift: "))

def caesar(original_tst,shifted_tst,encode_or_decode):
    output=""
    for letter in original_tst:
        if encode_or_decode == "decode":
            shifted_tst*=-1
        shifted_position=alphabet.index(letter)+shifted_tst
        shifted_position%=len(alphabet)
        output+=alphabet[shifted_position]
    print(f"Here is the {encode_or_decode}d result: {output}")
caesar(text,shift,direction)
