#Exercise 1 : Use the terminal
print("**** exercise 1 ****")
print('the PATH variable stores directories where executable files are located.Because the folder containing python.exe is added to PATH during installation, I can run python from any directory without being in the Python folder.')

#Exercise 2 : Alias
print("**** exercise 2 ****")
print('i did')

# Exercise 3 : Outputs
print("**** exercise 3 ****")
print(3 <= 3 < 9) #true
print(3 == 3 == 3)#true
print(bool(0))#false
print(bool(5 == "5"))#false
print(bool(4 == 4) == bool("4" == "4"))#true
print(bool(bool(None)))#false
x = (1 == True)
y = (1 == False)
a = True + 4
b = False + 10
print("x is", x)#true
print("y is", y)#false
print("a:", a)#5
print("b:", b)#10

#Exercise 4 : How many characters in a sentence ?
my_text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit,            sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.            Ut enim ad minim veniam, quis nostrud exercitation ullamco            laboris nisi ut aliquip ex ea commodo consequat.            Duis aute irure dolor in reprehenderit in voluptate velit            esse cillum dolore eu fugiat nulla pariatur.            Excepteur sint occaecat cupidatat non proident,            sunt in culpa qui officia deserunt mollit anim id est laborum."
print(len(my_text))

#Exercise 5: Longest word without a specific character
longest_sentence = ""

while True:
    sentence = input("Enter the longest sentence you can without the letter 'A': ")

    # Check if the sentence contains 'A' or 'a'
    if 'a' in sentence.lower():
        print("Oops! Your sentence contains the letter 'A'. Try again.")
        continue

    # Check if this sentence is longer than the current longest
    if len(sentence) > len(longest_sentence):
        longest_sentence = sentence
        print("Congratulations! This is the new longest sentence without 'A'!")
    else:
        print("Your sentence is valid but not longer than the current longest.")
