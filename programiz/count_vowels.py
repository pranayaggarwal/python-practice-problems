
def countVowels(str):
    vowelstr = "aeiou"
    vowels = {}.fromkeys(vowelstr, 0) # defulat value 0

    for i in str:
        if vowels.get(i, -1) != -1:  # if i in vowels
            vowels[i] +=1
    
    return vowels;

ip_str = 'Hello, have you tried our tutorial section yet?'
print(countVowels(ip_str))