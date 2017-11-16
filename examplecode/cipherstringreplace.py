def cipher(text, code):
    i = 0
    for old_letter in "abcdefghijklmnopqrstuvwxyz":
        
        if old_letter in text:
            text = text.replace(old_letter, code[i])
        i = i + 1
        
    return text
            
def main():
    new_text = cipher("how do you do", "ZYXWVUTSRQPONMLKJIHGFEDCBA")
    print(new_text)
    
if __name__ == "__main__":
    main()
