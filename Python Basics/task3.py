#    String

# Q.1 Take a String input and print its length.
str=input("Enter a string: ")
# to clauculate length of string.
str_len=len(str)
print("Length of the string is:", str_len)


# Q.2 Convert a sentence to Lowercase.
sen=input("Enter a sentence: ")
# to convert sentence to lowercase.
sen_lower=sen.lower()
print("Lowercase sentence is:", sen_lower)


# Q.3 Replace spaces with underscores in a string.
str=input("Enter a string: ")
# to replace spaces with underscores.
str_replace=str.replace(" ", "_")
print("String after replacing spaces with underscores:", str_replace)


# Q.4 Extract the First and Last Character of a String.
str=input("Enter a string: ")
# to extract first and last character of string.
first_char=str[0]
last_char=str[-1]
print("First character of the string is:", first_char)
print("Last character of the string is:", last_char)


# Q.5 Reverse a String using Slicing.
str=input("Enter a string: ")
# to reverse a string using slicing.
str_reverse=str[::-1]
print("Original string is:", str)
print("Reversed string is:", str_reverse)


# Q.7 Count How many Times a letter appears in a String.
str=input("Enter a string: ")
letter=input("Enter a letter to count its occurrences: ")
# to count how many times a letter appears in a string.
count=str.count(letter)
print("The letter '{}' appears {} times in the string.".format(letter, count))


# Q.8 Check if a word is present in a sentence.
sen=input("Enter a sentence: ")
word=input("Enter a word to check its presence: ")
# to check if a word is present in a sentence.
if word in sen:
    print("The word '{}' is present in the sentence.".format(word))
else:
    print("The word '{}' is not present in the sentence.".format(word))


# Q.9 Take name & age and print using f-string formatting.
name=input("Enter your name: ")
age=input("Enter your age: ")
# to print name and age using f-string formatting.
print(f"Name: {name}, Age: {age}")


# Q.10 Remove extra spaces from the start and end of a string.
str=input("Enter a string with extra spaces: ")
# to remove extra spaces from the start and end of a string.
str_trimmed=str.strip()
print("String after removing extra spaces:", str_trimmed)


# Q.11 Join a list of words into a single string with - between them.
words = input("Enter a list of words separated by spaces: ").split()
# to join a list of words into a single string with '-' between them.
joined_string = '-'.join(words)
print("Joined string with '-' between words:", joined_string)


#    List Operation

# Q.12 Create a list of your 5 favorite movies.
movies = ["Jailer","Jailer 2","Toxic","Vikram","LEO"]
print("Five Favorite Movies : ",movies)

# add a new movie to the list.
add_movie = "jailer 3"
movies.append(add_movie)
print("Updated list of movies:", movies)

# Remove the first movie from the list.
remove_movie = movies.pop(0)
print("Updated list of movies:", movies)


# Q.13 Sort a list of numbers in ascending order.
num=[5,1,4,3,8,9]
#sort in ascending order
ascen=sorted(num)
print("Ascending order:",ascen)
        # OR
num.sort()
print("Ascending order :",num)        


# Q.14 reverse a list
num.reverse()
print("Reverse order:",num)
         # OR
rev=reversed(num)
print("Reverse order:",list(rev))

# Q.15 Find the largest number in a list.
largest_no = max(num)
print("Largest number:",largest_no)


# Q.16 Merge two lists into one.
fruits = ["apple", "banana", "cherry"]
vegetables = ["carrot", "tamato", "onion"]
# merge two lists
merge=fruits+vegetables
print("Merge two lists:",merge)


# Q.17 Access the last element of a list without using index no. .
fruits=["apple", "banana", "cherry", "orange"]
# print last element without using index number .
last_element=fruits[-1]
print("Last element:",last_element)


# Q.18 Create a nested list and acces a specfic inner element.
num=[[1,2,3],[4,5,6],[7,8,9]]
# access inner element
print("Access inner element:",num[1][0])


# Q.19 Count how many times an element appears in a list.
num=[1,2,1,3,4,5,2,1,4]
# count times of an element appears in a list
count=num.count(1)
print("count appears of elements :",count)
