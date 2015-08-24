# -*- coding: utf-8 -*-
"""
Created on Fri Sep 19 16:05:41 2014

@author: mjbeck

The game of hangman with text based interface
"""

import random
import sys

wordfile = r'C:\Users\mjbeck\Python\python-3.3.3.amd64\Scripts\mjbeck\wordlist.txt'

def word_guessed(secret_word,letters_guessed):
    """ check if all letters of secret word have been guessed """
    # check if secret word is a subset of (or equivalent to) letters guessed
    # use sets to reduce out duplcates
    if set(secret_word)<=set(letters_guessed):
        return True
    return False

def print_guessed(secret_word,letters_guessed):
    """ build a string of the secret word with guessed letters and underscores """
    output = ''
    for i in secret_word:
        if i in letters_guessed:
            output = output + i
        else:
            output = output + '_'
    return output

def hangman(MAX_GUESSES):
    """ Summary  : main loop for hangman game
                   guess the (random) secret word one letter at a time
        Input    : MAX_GUESSES = integer number of incorrect letter guesses before game over
        Output   : text based game status
    """
    wordlist        = build_wordlist(wordfile)
    secret_word     = random.choice(wordlist).upper()
    letters_guessed = []
    mistakes_made   = 0

    while mistakes_made < MAX_GUESSES:
        print('\nYou have %s chances left to guess: %s' % ((MAX_GUESSES - mistakes_made), print_guessed(secret_word, letters_guessed)))
        guess = input('Enter your next letter guess: ').upper()
        letters_guessed += guess
        if guess in secret_word:
            if word_guessed(secret_word,letters_guessed):
                print('\n\nThe word was %s \nYou Won!\n' % print_guessed(secret_word,letters_guessed))
                break
            else:
                print('On the right track, keep going!\n')
        else:
            mistakes_made += 1;
            if mistakes_made >= MAX_GUESSES:
                print('\nYou ran out of chances! \n You Lost! \n')
                print('The secret word was '+secret_word)
    choice = input('\nWould you like to play again? Y/N: ').upper()
    if 'Y' in choice:
        hangman(MAX_GUESSES)


def build_wordlist(wordfile):
    """ read list of words from file, keep words if 3 or more letters, no ', and
        first letter is lower case
    """
    with open(wordfile,'r') as fob:
        wordlist = fob.read().split()
    keeplist = []
    for word in wordlist:
        if (len(word)>3) & (word.find("'") == -1) & (word[0].islower()):
            keeplist.append(word)
    return keeplist

if __name__ == '__main__':
    if len(sys.argv)>1:
        hangman(int(sys.argv[1]))
    else:
        MAX_GUESSES = 8
        hangman(MAX_GUESSES)
