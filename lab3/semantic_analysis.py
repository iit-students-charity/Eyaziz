from nltk.corpus import wordnet as wn
import nltk
import time
symbols = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '.', ',', '!', '№', ';', ':', '?', '(', ')', '"', '\'', '-',
           "\n", '«', '»']


def semantic_analysis(way='', text=''):
    start_loop = time.time()
    nltk.download('wordnet')
    words = []
    if way == '':
        words = text.split(' ')
    if text == '':
        file = open(f'{way}', 'r', encoding="utf-8")
        words = file.read().split(' ')
        file.close()

    for i in range(len(words)):
        for j in symbols:
            if words[i].count(j):
                words[i] = words[i].replace(f"{j}", "")
    for i in range(len(words)):
        words[i] = words[i].lower()
    new_file = open("semantic_analysis.txt", 'w')
    for i in words:
        examples = []
        synonyms = []
        antonyms = []
        hyponyms = []
        hypernyms = []
        syn = wn.synsets(i)

        if len(syn[0].definition()) == 0:
            new_file.write(f'{i.capitalize()}.\n')
        else:
            new_file.write(f'{i.capitalize()} - {syn[0].definition()}.\n')


        if len(syn[0].examples()) == 0:
            examples = None
        else:
            examples = str(syn[0].examples())
            examples = examples.replace('[', '')
            examples = examples.replace(']', '')
            examples = examples.replace("'", '')
            new_file.write(f'Example: {examples}.\n')

        for syn in wn.synsets(i):
            for l in syn.lemmas():
                synonyms.append(l.name())
                if l.antonyms():
                    antonyms.append(l.antonyms()[0].name())
        if len(synonyms) == 0:
            synonyms = None
        else:
            synonyms = str(set(synonyms))
            synonyms = synonyms.replace('{', '')
            synonyms = synonyms.replace('}', '')
            synonyms = synonyms.replace("'", '')
            new_file.write(f'Synonyms: {synonyms}.\n')

        if len(antonyms) == 0:
            antonyms = None
        else:
            antonyms = str(set(antonyms))
            antonyms = antonyms.replace('{', '')
            antonyms = antonyms.replace('}', '')
            antonyms = antonyms.replace("'", '')
            new_file.write(f'Antonyms: {antonyms}.\n')

        for h in syn.hyponyms():
            hyponyms.append(h.name()[0:-5])
        for h in syn.hypernyms():
            hypernyms.append(h.name()[0:-5])
        if len(hypernyms) == 0:
            hypernyms = None
        else:
            hypernyms = str(hypernyms)
            hypernyms = hypernyms.replace('[', '')
            hypernyms = hypernyms.replace(']', '')
            hypernyms = hypernyms.replace("'", '')
            new_file.write(f'Hypernyms: {hypernyms}.\n')
        if len(hyponyms) == 0:
            hyponyms = None
        else:
            hyponyms = str(hyponyms)
            hyponyms = hyponyms.replace('[', '')
            hyponyms = hyponyms.replace(']', '')
            hyponyms = hyponyms.replace("'", '')
            new_file.write(f'Hyponyms: {hyponyms}.\n')

        new_file.write('-------------------------------------------\n\n')
    new_file.close()
    end_loop = time.time()
    print('Время посчёта', end_loop - start_loop)
