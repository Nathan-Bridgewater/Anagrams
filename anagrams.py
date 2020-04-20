"""Find all the anagrams of a user inputted word and ouput them in a
neatly formatted way. Example word: pots"""
import load_dictionary


# Load the dictionary into a list of words
filename = '2of4brif.txt'
words = load_dictionary.load_file(filename)

# input a SINGLE word or SINGLE name below to find its anagram(s)
user_word = input('Enter a word to be searched for anagrams: ')
user_word = user_word.lower()
print(f"Word for analysis: {user_word}")

anagrams = []

# Loop through words in dictionary and determine if the word is an anagram
for word in words:
    word = word.lower()

    # Omit the word if it is the same as one in the dictionary
    if word != user_word:
        if sorted(word) == sorted(user_word):
            anagrams.append(word)

# print a list of the anagrams
if len(anagrams) == 0:
    print('That word has no anagrams in the dictionary you have selected')
else:
    print("Anagrams = ", *anagrams, sep='\n')


