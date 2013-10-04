# Things you should be able to do.
# Write a function that takes a list and returns a new list with only the odd numbers.
def all_odd(some_list):
    odd_list = []
    for i in some_list:
        if i % 2 == 1:
            odd_list.append(some_list[i])
    return odd_list
print "These are the odd items:", all_odd([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

# Write a function that takes a list and returns a new list with only the even numbers.
def all_even(some_list):
    even_list = []
    for i in some_list:
        if i % 2 == 0:
            even_list.append(some_list[i])
    return even_list
print "These are the even items:", all_even([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

# Write a function that takes a list of strings and returns a new list with all strings of length 4 or greater.
def long_words(word_list):
    new_list = []
    for i in word_list:
        if len(i) >= 4:
            new_list.append(i)
    return new_list

print "This is the longest word:", long_words(["Hello", "my", "name", "is", "Mica", "and", "I", "hate", "asparagus."])

# Write a function that finds the smallest element in a list of integers and returns it.
def smallest(some_list):
    smallest = some_list[0]
    for i in some_list:
        if i <= smallest:
            smallest = i
    return smallest
print "This is smallest integer in the list:", smallest([100, 1, 2, 3, 4, 0, 25])

# Write a function that finds the largest element in a list of integers and returns it.
def largest(some_list):
    largest = some_list[0]
    for i in some_list:
        if i >= largest:
            largest = i
    return largest
print "This is the largest integer in the list:", largest([100, 1, 2, 3, 4, 1000, 0, 25])

# Write a function that takes a list of numbers and returns a new list of all those numbers divided by two.
def halvesies(some_list):
    new_list = []
    for i in some_list:
        new_list.append(i/2)
    return new_list

print "This is every list item divided by two:", halvesies([2, 4, 6, 8, 10])

# Write a function that takes a list of words and returns a list of all the lengths of those words.
def word_lenths(word_list):
    new_list = []
    for i in word_list:
        new_list.append(len(i))
    return new_list

print "This is the length of every word:", word_lenths(["Hello", "my", "name", "is", "Mica", "and", "I", "am", "at", "Hackbright."])

# Write a function (using iteration) that sums all the numbers in a list.
def sum_numbers(numbers):
    total = 0
    for i in numbers:
        total += i
    return total

print "This is the sum of the items in the list:", sum_numbers([0, 1, 2, 3])

# Write a function that multiplies all the numbers in a list together.
def mult_numbers(numbers):
    product = 1
    for i in numbers:
        product = product * i
    return product

print "This is all the items multiplied by each other:", mult_numbers([1, 2, 3, 4, 5])

# Write a function that joins all the strings in a list together (without using the join method) 
# and returns a single string.
def join_strings(string_list):
    string = ""
    for i in string_list:
        string += i
    return string

print "This joins all the items together:", join_strings(["This", " ", "is", " ", "a", " ", "string", "."])

# Write a function that takes a list of integers and returns the average (without using the avg method)
def average(numbers):
    the_sum = 0
    for i in numbers:
        the_sum += i
    return (float(the_sum)/len(numbers))
print "This is the average of the list integers:", average([4,3])