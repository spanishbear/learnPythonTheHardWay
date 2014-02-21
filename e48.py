uInput = raw_input('> ')
words = uInput.split()

def combiner(firWord, keyword):
    pair = []
    pair = [firWord, keyword]
    return pair    

def directions(compass):
    first_word = 'direction'
    pair = combiner(first_word, compass)
    print "This is the following tuple: %s" % pair

def verbs(moves):
    first_word = 'verbs'
    pair = combiner(first_word, moves)
    print "This is the following tuple: %s" % pair

def nouns(ppt):
    first_word = 'noun'
    pair = combiner(first_word, ppt)
    print "This is the following tuple: %s" % pair

def stops(other):
    first_word = 'stop'
    pair = combiner(first_word, other)
    print "This is the following tuple: %s" % pair


def error(warning):
    pair = []
    first_word = 'error'
    second_word = warning
    pair = [first_word, second_word]
    print "This is the following tuple: %s" % pair


for word in words: 
    if word == "north" or word == "south" or word == "east" or word == "west":
        #print "Direction word(s): % s" % word
        directions(word)
    elif word == "go" or word == "stop" or word == "kill" or word == "eat":
        #print "Stop word(s): % s" % word
        verbs(word)
    elif word == "door" or word == "bear" or word == "princess":
        #print "Noun(s): % s" % word
        nouns(word)
    elif word == "the" or word == "in" or word == "of" or word == "from" or word == "at" or word == "it":
        stops(word)
