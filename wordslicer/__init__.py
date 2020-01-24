from math import log
import re
import pprint
import subprocess
import sys
from getopt import getopt
import fileinput
from collections import Counter
import matplotlib.pyplot as plt


def __wordsByFrequency(words):
    return Counter(words)


def __getAllWords(text):
    # Convert to lowercases
    # text = text.lower()
    
    # Replace all none alphanumeric characters with spaces
    #text = re.sub(r'[^a-zA-Z0-9\s\n\.!]', ' ', text)
    
    # Break sentence in the token, remove empty tokens
    return re.findall(r'\w+',text)



def train(filename):
    text = ""
    for line in fileinput.input(filename):
        text += line

    words = __getAllWords(text)

    with open('words.txt', 'w') as f:
        for item in words:
            f.write("%s\n" % item)
    c = __wordsByFrequency(words)

    with open('dict.txt', 'w') as f:
        for item in c.keys():
            f.write("%s\n" % item)
    return c



def separate(words_by_frequency, text):

   
    # Build a cost dictionary, assuming Zipf's law and cost = -math.log(probability).
    total_words = sum(words_by_frequency.values())
    maxword = max(len(x) for x in words_by_frequency.keys())

    wordcost = dict((word, log((count+1)*log(total_words))) for word, count in words_by_frequency.items())

    # Find the best match for the i first characters, assuming cost has
    # been built for the i-1 first characters.
    # Returns a pair (match_cost, match_length).
    def best_match(i):
        candidates = enumerate(reversed(cost[max(0, i-maxword):i]))
        return min((c + wordcost.get(text[i-k-1:i], 9e999), k+1) for k,c in candidates)


    # Build the cost array.
    cost = [0]
    for i in range(1, len(text) + 1):
        c, k = best_match(i)
        cost.append(c)

    # Backtrack to recover the minimal-cost string.
    out = []
    i = len(text)
    while i>0:
        c,k = best_match(i)
        assert c == cost[i]
        out.append(text[i-k:i])
        i -= k

    return " ".join(reversed(out))



def plot(wrong, total):
    # wrong_percentage = wrong/total
    # correct_percentage = (total-wrong)/total
    
    labels = ['Wrong', 'Correct']
    sizes = [wrong, (total-wrong)]
    colors = ['lightcoral', 'limegreen']
    explode = (0.1, 0)
    fig1, ax1 = plt.subplots()
    patches = plt.pie(sizes, explode=explode, autopct='%1.1f%%', colors=colors, shadow=False, startangle=90, wedgeprops={"edgecolor":"0",'linewidth': 1, 'antialiased': True})
    plt.legend(patches[0], labels, loc="best")
    ax1.axis('equal')
    plt.tight_layout()
    plt.show()

def evaluate(output, correct):
    output_words = __wordsByFrequency(__getAllWords(output))
    words_correct = __wordsByFrequency(__getAllWords(correct))

    total_words = sum(words_correct.values())
    wrong_words = 0
    
    for word, occurences in output_words.items():
        wrong_words = occurences - words_correct.get(word, 0)

    plot(wrong_words, total_words)



# Setup for testing

opts, resto = getopt(sys.argv[1:], "t:s:")
dop = dict(opts)

model = {}

if "-t" in dop: # train
    model = train(dop["-t"])
    
    if "-s" in dop: # separate
        text = ""
        for line in fileinput.input(dop["-s"]):
            text += line

        output = separate(model, text)
        to_compare = "My name is Frodo. Hello Gandalf. I was born in 1418! When Mr Bilbo Baggins of Bag End announced that he would shortly be celebrating."
        
        print(output)
        
        evaluate(output, to_compare)

else:
    print("Make sure the parameters are correct.")


