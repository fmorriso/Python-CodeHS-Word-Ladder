"""
CodeHS 7.3.9 - Word Ladder
1. Ask your friend for an initial word
2. Repeatedly ask them for an index and a letter
3. You should replace the letter at the index they provided with the letter they enter
4. You should then print the new word
5. Stop asking for input when the user enters -1 for the index
"""
INVALID_INDEX_ERROR_MESSAGE = 'invalid index'

def get_index():
    i = -1
    while True:
        try:
            i = int(input(f'Enter an index between 0 and {max_index} or -1 to quit: '))
            if -1 <= i < len(word): # WARNING: CodeHS auto grader does not allow max_index here
                return i
            print(INVALID_INDEX_ERROR_MESSAGE)
        except ValueError:
            print(INVALID_INDEX_ERROR_MESSAGE)



def get_letter():
    # Must be exactly one character!
    # character must be a lowercase letter!
    c = ''
    while True:
        c = input('Enter a letter: ')
        if len(c) != 1:
            print('Must be exactly one character!')
        elif c != c.lower():
            print('Character must be a lowercase letter!')
        else:
            return c


word = input('Enter a word: ')
max_index = len(word) - 1
# print(f'{word=}')
letters = list(word)
# print(f'{letters=}')
while True:
    idx = get_index()
    if idx == -1:
        break
    letter = get_letter()
    # print(f'{letter=}')
    letters[idx] = letter
    word = "".join(letters)
    print(word)
