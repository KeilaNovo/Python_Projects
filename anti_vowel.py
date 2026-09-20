def anti_vowel(text):
    vowels = 'aeiouAEIOU'
    textlist = []
    for char in text:
        if char in vowels:
            continue
        else: 
            textlist.append(char)      
    return "".join(textlist)  


#To remove the vowels in a string
