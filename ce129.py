'''
reverse_vowels("Hello!") # "Holle!"
reverse_vowels("Tomatoes") # "Temotaos"
reverse_vowels("Reverse Vowels In A String") # "RivArsI Vewols en e Streng"
reverse_vowels("aeiou") # "uoiea"
reverse_vowels("why try, shy fly?") # "why try, shy fly?"
'''


def reverse_vowels(string):
    vowels = 'aeiouAEIOU'
    vowels_in = [letter for letter in string if letter in vowels]
    answer = []
    for char in string:
        if char not in vowels:
            answer.append(char)
        else:
            poped_char = vowels_in.pop()
            answer.append(poped_char)
    return ''.join(answer)


print(reverse_vowels("Hello!"))
print(reverse_vowels("Tomatoes"))
print(reverse_vowels("Reverse Vowels In A String"))
print(reverse_vowels("aeiou"))
print(reverse_vowels("why try, shy fly?"))
