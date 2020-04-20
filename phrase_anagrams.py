import sys
from collections import Counter
import load_dictionary

dict_file = load_dictionary.load_file('2of4brif.txt')
# Ensure "a" and "i" are included
dict_file.append('a')
dict_file.append('i')
dict_file = sorted(dict_file)

# Take users name
ini_name = input("Enter a name: ")
ini_name = ini_name.lower()


def find_anagrams(name, word_list):
    """Read name and dictionary file and display all anagrams in name"""
    # Form a dictionary of the name in the form of "letter: number of letter"
    name_letter_map = Counter(name)
    anagrams = []

    # Loop through every word in the dictionary
    for word in word_list:
        # test string holds all the letters in dictionary word available to use
        test = ''
        word_letter_map = Counter(word.lower())
        for letter in word:
            # add letters to test if they fit into the name
            # and confirm if the it is the full dictionary word
            if word_letter_map[letter] <= name_letter_map[letter]:
                test += letter
            if Counter(test) == word_letter_map:
                anagrams.append(word)

    # Display information
    print('ANAGRAMS:')
    print(*anagrams, sep='\n')
    print()
    print(f"Remaining letters = {name}")
    print(f"Number of remaining letter {len(name)}")
    print(f"Number of remaining anagrams = {len(anagrams)}")


def process_choice(name):
    """Check users choice for validity, return choice and leftover letters"""
    while True:
        # Prompt for input of user to pick anagrams
        choice = input("\nMake a choice, Enter to start over, # to end: ")

        if choice == '':
            main()

        elif choice == '#':
            sys.exit()

        else:
            # form a string containing all the letters entered by user
            candidate = ''.join(choice.lower().split())
            left_over_list = list(name)
            for letter in candidate:
                # Remove each letter in the anagram(s) from the name
                if letter in left_over_list:
                    left_over_list.remove(letter)

            # if the letters taken away from the original "name" word
            # match the candidate word then succesfull choice
            if len(name) - len(left_over_list) == len(candidate):
                break
            else:
                print('Wont work! Make another choice!', file=sys.stderr)

    name = ''.join(left_over_list)
    return choice, name


# Main program loop
def main():
    """Help user build anagram phrases from their name"""
    name = ''.join(ini_name.lower().split())
    name = name.replace('-', '')

    limit = len(name)
    phrase = ''
    running = True

    while running:
        # remove white space from the phrase
        temp_phrase = phrase.replace(' ', '')

        # continue to find anagrams if the length of the phase is smaller than
        # the length of the initial name
        if len(temp_phrase) < limit:
            print(f'The length of the anagram phrase = {len(temp_phrase)}')
            find_anagrams(name, dict_file)
            print(f"\nCurrent anagram phrase = {phrase}", file=sys.stderr)
            choice, name = process_choice(name)
            phrase += choice + ' '

        # If you reach the limit finish the program
        elif len(temp_phrase) == limit:
            print("\n*****FINISHED*****\n")
            print(f"Anagram of name = {phrase}",file=sys.stderr)
            try_again = input('\n\nTry again? (press "n" to quit)\n ')
            if try_again.lower() == "n":
                running = False
                sys.exit()
            else:
                main()


if __name__ == '__main__':
    main()
