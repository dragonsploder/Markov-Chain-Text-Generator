from collections import defaultdict
from random import choice
import json
import sys

# Remove encoding="utf8" for non windows machines

def genChain(filePath, gramSize):
    corpusFile = open(filePath, encoding="utf8")
    corpus = corpusFile.read()
    chain = {}
    corpus = corpus.replace("\n", " ")
    corpus = corpus.split(" ")
    if gramSize == 1:
        for i in range(len(corpus)-1):
            if corpus[i] in chain:
                if corpus[i+1] not in chain[corpus[i]]:
                    chain[corpus[i]].append(corpus[i+1])
            else:
                chain[corpus[i]] = [corpus[i+1]]
        return chain
    elif gramSize > 1:
        for i in range(len(corpus)-gramSize):
            Key = corpus[i]
            for a in range(gramSize-1):
                Key = Key + " " + corpus[i+a+1]
            if Key in chain:
                if corpus[i+gramSize] not in chain[Key]:
                    chain[Key].append(corpus[i+gramSize])
            else:
                chain[Key] = [corpus[i+gramSize]]
        return chain

def getStarts(chain):
    startingWords = []
    for word in chain:
        try:
            if word[0].isupper():
                startingWords.append(word)
        except:
            pass
    return startingWords

def genSentance(chain, gramSize):
    startingWords = getStarts(chain)
    previousWord = choice(startingWords)
    sentance = [previousWord]
    i = 0
    if gramSize == 1:
        while "." not in sentance[i] and "!" not in sentance[i] and "?" not in sentance[i]:
            previousWord = choice(chain[previousWord])
            sentance.append(previousWord)
            i += 1
        sentance = " ".join(sentance)
        return sentance
    elif gramSize > 1:
        while "." not in sentance[i] and "!" not in sentance[i] and "?" not in sentance[i]:
            shift = previousWord.split(" ")
            word = shift[0]
            del shift[0]
            shift = " ".join(shift)
            previousWord = shift + " " + choice(chain[previousWord])
            sentance.append(word)
            i += 1
        del sentance[0]
        sentance = " ".join(sentance)
        return sentance


def printHelp():
    print("""Markov Text Generater
Arguments
    -h: This help
    Necessary:
        -g [Gram Size]

        -f [Corpus File path]
        or
        -l [Load Chain File Path]
    Optional:
        -s [Save Chain File Path]
        -c show only chain
    """)

def main():
    gramSize = None
    filePath = None
    loadPath = None
    savePath = None
    showChain = False
    for i in range(len(sys.argv)):
        if sys.argv[i] == "-h":
            printHelp()
            exit(0)
        if sys.argv[i] == "-f":
            filePath = sys.argv[i+1]
        if sys.argv[i] == "-s":
            savePath = sys.argv[i+1]
        if sys.argv[i] == "-l":
            loadPath = sys.argv[i+1]
        if sys.argv[i] == "-g":
            gramSize = sys.argv[i+1]
            gramSize = int(gramSize)
        if sys.argv[i] == "-c":
            showChain = True
    if filePath == None and loadPath == None:
        print("No file specified. Abort")
        exit(0)
    elif gramSize == None:
        print("Gram size unspecified. Abort")
        exit(0)


    if filePath != None:
        chain = genChain(filePath, gramSize)
    else:
        loadFile = open(loadPath, 'r', encoding="utf8")
        chain = json.load(loadFile)
        loadFile.close()

    if savePath != None:
        saveFile = open(savePath, 'w', encoding="utf8")
        json.dump(chain, saveFile)
        saveFile.close()

    if showChain:
        for i in chain:
            print(i + " : ", end="")
            print(chain[i])
    else:
        sentance = genSentance(chain, gramSize)
        print(sentance)

main()