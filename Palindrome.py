# Check whether the given string is palindrome or not. A palindrome is a word, number, phrase, or other sequence of characters which reads the same backward as forward.
word = input("Enter the word to check palindrome")
if word == word[::-1]:
    print("%s is palindrome" % word)
else:
    print("%s is not palindrome..." % (word))
