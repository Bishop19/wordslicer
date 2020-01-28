from math import log
import re
import fileinput
from collections import Counter
import matplotlib.pyplot as plt


def __wordsByFrequency(words):
    return Counter(words)


def __getAllWords(text):
    return re.findall(r'\w+',text)



def train(filename):
    text = ""
    for line in fileinput.input(filename):
        text += line

    words = __getAllWords(text)
    words_by_frequency = __wordsByFrequency(words)

    total_words = sum(words_by_frequency.values())
    maxword = max(len(x) for x in words_by_frequency.keys())

    wordcost = dict((word, log((rank+1)*log(total_words))) for rank, word in enumerate(words_by_frequency.keys()))

    return (wordcost, maxword)



def __separate(model, text):
    wordcost = model[0]
    maxword = model[1]

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


def separate(model, text):
    x = 0
    output = ""
    while len(text)>0:
        x = re.search(r'[!.,?;\'\n"()\-:]', text)
        if x != None: 
            y = x.start()
            if x.group(0) != '\n' and x.group(0) != '\'':
                output += __separate(model, text[:y]) + x.group(0) +" "
                text = text[y+1:]
            else:
                output += __separate(model, text[:y]) + x.group(0)
                text = text[y+1:]     
        else:
            output += __separate(model, text) + " "
            break
    
    return output


def join(model, text):
    text = re.sub(r' ', r'', text)

    return separate(model, text)


def __plot(wrong, correct):    
    labels = [f'Wrong ({wrong})', f'Correct ({correct})']
    sizes = [wrong, correct]
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

    total_words = sum(output_words.values())
    wrong_words = 0
    
    for word, occurences in output_words.items():
        wrong_words += occurences - words_correct.get(word, 0)

    __plot(wrong_words, total_words - wrong_words)


def save(filename, text):
    with open(filename, 'w') as f:
        f.write(text)



