import random
import string
import time
import multiprocessing
from multiprocessing import Process

foundWords = []
hamFoundWords = []
foundWords = []

with open('free_use_dictionary.txt', 'r') as f:
    dict = f.readlines()
for i, item in enumerate(dict):
    dict[i] = item.split('\n')[0]
dict = set(dict)
ham = []
with open('hamlet.txt', 'r') as f:
    for line in f:
        for word in line.split():
           ham.append((word.translate(str.maketrans('', '', string.punctuation))).lower())
ham = set(ham)

def monkey(name):
    totString = ""
    longestWord = ""
    t0 = time.time()
    while True:
        if time.time()-t0>10:
            print("\n")
            print("This is the monkey " + name)
            print("\n")
            print("LONGEST HAMLET WORD FOUND:")
            print(longestWord)
            print("\n")
            print("HAMLET FOUND WORDS")
            print(hamFoundWords)
            print("\n")
            print("ALL FOUND WORDS: ")
            print(foundWords)
            print("\n")
            print("\n")
            t0=time.time()

        randomGenLet = random.choice(string.ascii_letters).lower()
        tempList = list(totString)
        for i, item in enumerate(tempList):
            tester = "".join(tempList[-i:])
            if tester in ham and len(tester)>1: 
                if len(tester) > len(longestWord):
                    longestWord = tester
                ham.remove(tester)
                hamFoundWords.append(tester)
            if tester in dict and len(tester)>2:
                foundWords.append(tester)
        totString += randomGenLet


if __name__ == '__main__':
    inputs = ['quincy','adam','james','spoon','shrimp bucket','horse','fig newton','agro','stabby','chokey']
    pool = multiprocessing.Pool(processes=10)
    pool.map(monkey, inputs)

    