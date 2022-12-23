
import os
import sys
import random

def one_tg(key, character1):
    def markov_lib(key, character1):
        data_sample = "moby-dick.txt"
        text_data = open(data_sample, 'r').read()
        text_data = ''.join([i for i in text_data if not i.isdigit()]).replace("\n", " ").split(' ')
        markov_lib = {}

        for i in range(len(text_data)-key):
            word = " ".join(text_data[i:i+key])
            if word.lower() in markov_lib.keys():
                markov_lib[word.lower()].append(text_data[i+key])
            else:
                markov_lib[word.lower()] = [text_data[i+key]]

        try:
            character2 = random.choice(markov_lib[character1.lower()])
        except KeyError as e:
            return ("fail")
        return character2
        
    sentence_stopper = ['.', '?', '!']
    message = character1.capitalize()
    while message[-1] not in sentence_stopper:
        try:
            character2 = markov_lib(key,character1)
            message += " " + character2
            character1 = " ".join((message.split())[-(key):])
        except KeyError as e:
            print("-------------------------\nThe training text is not big enough to generate the next word. Exited")
    return message

def two_tg(key,character1,word_count):
    def markov_lib(key, character1):
        data_sample = "moby-dick.txt"
        text_data = open(data_sample, 'r').read()
        text_data = ''.join([i for i in text_data if not i.isdigit()]).replace("\n", " ").split(' ')
        markov_lib = {}

        for i in range(len(text_data)-key):
            word = " ".join(text_data[i:i+key])
            if word.lower() in markov_lib.keys():
                markov_lib[word.lower()].append(text_data[i+key])
            else:
                markov_lib[word.lower()] = [text_data[i+key]]

        try:
            character2 = random.choice(markov_lib[character1.lower()])
        except KeyError as e:
            return ("fail")
        return character2
        
        message = character1.capitalize()
    message = character1.capitalize()
    for i in range(word_count):
        try:
            character2 = markov_lib(key,character1)
            message += " " + character2
            character1 = " ".join((message.split())[-(key):])
        except KeyError as e:
            print("-------------------------\nThe training text is not big enough to generate the next word. Exited")
    return message


