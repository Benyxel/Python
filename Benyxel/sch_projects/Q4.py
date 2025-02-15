def count_vowels():
    user_input = input("Enter a string: ")
    if user_input == '':
        print("You did not enter a string.")
    vowel_count = 0
    vowels = "aeiou"
    vowels = vowels.lower()
    for letter in user_input:
        if letter in vowels:
            vowel_count += 1
            
    print("Number of vowels:", vowel_count)
        
count_vowels()            
