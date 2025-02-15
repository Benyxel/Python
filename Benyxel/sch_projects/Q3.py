

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
def filter_even(numbers):

    even_numbers = []
    for number in numbers:
        if number % 2 == 0:
            even_numbers.append(number)
    return even_numbers
    
even_number = filter_even(numbers)
print(even_number)    

