import re


def is_palindrome(phrase):
    phrase = phrase.lower()
    regex = re.compile('[^a-zA-Z]')
    phrase = re.sub(regex, '', phrase)

    if phrase == phrase[::-1]:
        return True
    return False


phrase = input("Enter a phrase to see if it is a palindrome: ")
print(is_palindrome(phrase))
