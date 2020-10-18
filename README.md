# Simple Markov Chain Text Generator
Generate random text from corpus

Inspired by this [video](https://youtu.be/3AjlsTtrfVY)

Uses python 3

## How To Use
Generate a sentence
```
$ python markov.py -f corpus.txt -g 1
```

Save chain to file
```
$ python markov.py -f corpus.txt -g 1 -s chain.txt
```

Load chain from file
```
$ python markov.py -l chain.txt -g 1
```

View chain
```
$ python markov.py -l chain.txt -g 1 -c
```

Help
```
$ python markov.py -h
```