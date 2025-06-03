def count_vowels(user_input): 
    if user_input == '':
        print("You did not enter a string.")
    vowel_count = 0
    vowels = "aeiou"
    # print(vowels)
    small = user_input.lower()
    # print(small)
    for letter in small:
        if letter in vowels:
            vowel_count += 1
            
    print(f"Number of vowels:", {vowel_count})

user_input = input("Enter a string: ")      
count_vowels(user_input)            
