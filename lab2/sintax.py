import pymorphy2
from nltk import CFG
import time
"""
S Предложение 
NP существительное
VP Глагольная фраза 
PP Предложная фраза 
Det Детерминатор
N Существительное
V глагол
P предлог
"""


def parsing(text='', way=0):
    start_loop = time.time()

    morph = pymorphy2.MorphAnalyzer()

    def part_of_speech(word):  # метод определяющий часть речи слова
        word_dict = {"NOUN": "N", "ADJF": "P", "ADJS": "PP", "COMP": "P", "VERB": "V", "INFN": "V", "PRTF": "P",
                     "PRTS": "P", "GRND": "P", "NUMR": "N", "ADVB": "P", "NPRO": "N", "PRED": "V", "PREP": "Det",
                     "CONJ": "P", "PRCL": "Det", "INTJ": "P"}
        word_analyze = morph.parse(word)[0]
        return word_dict.get(word_analyze.tag.POS)

    symbols = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '.', ',', '!', '№', ';', ':', '?', '(', ')', '"', '\'', '-',
               "\n", '«', '»']
    sentence_list = []
    if text == '':
        file = open(f'{way}', 'r', encoding="utf-8")
        sentence_list = file.read().split(".")
        file.close()
    elif way == 0:
        sentence_list = text.split(".")

    file = open(f'sentence_tree.txt', 'tw', encoding='utf-8')
    for i in range(len(sentence_list)):
        for j in symbols:
            if sentence_list[i].count(j):
                sentence_list[i] = sentence_list[i].replace(f"{j}", "")
    for i in range(len(sentence_list)):
        word_list = sentence_list[i].split(' ')
        for j in range(word_list.count('')):
            word_list.remove('')
        if word_list == []:
            continue
        else:
            det_word_list = []
            for j in range(len(word_list)):
                det_word_list.append({f'{word_list[j]}': f'{part_of_speech(word_list[j])}'})
            V = ''
            Det = ''
            N = ''
            P = ''
            for k in det_word_list:
                # time.sleep(10)
                if list(k.values()) == ['N']:
                    N = N + f'{list(k.keys())} | '
                elif list(k.values()) == ['Det']:
                    Det = Det + f'{list(k.keys())} | '
                elif list(k.values()) == ['V']:
                    V = Det + f'{list(k.keys())} | '
                elif list(k.values()) == ['P']:
                    P = P + f'{list(k.keys())} | '

            N = N.replace("['", "")
            N = N.replace("']", "")
            V = V.replace("['", "")
            V = V.replace("']", "")
            P = P.replace("['", "")
            P = P.replace("']", "")
            Det = Det.replace("['", "")
            Det = Det.replace("']", "")
            N = N[:-2]
            V = V[:-2]
            P = P[:-2]
            Det = Det[:-2]

            grammar = CFG.fromstring(f"""
              S -> NP VP
              VP -> V NP | V NP PP
              PP -> P NP    
              V -> {V}
              NP ->  Det N | Det N PP
              Det -> {Det}
              N -> {N}
              P -> {P}
              """)
            sent = f'{sentence_list[i]}'.split()
            grammar.start()
            result = str(grammar.productions())
            result = result.replace('[', '')
            result = result.replace(']', '')
            result = result.replace(',', '\n')
            result = result.replace('S', 'Предложение')
            result = result.replace('NP', 'Именная группа')
            result = result.replace('VP', 'Глагольная группа')
            result = result.replace('PP', 'Предложная группа ')
            result = result.replace('Det', 'Детерминатор')
            result = result.replace('N', 'Существительное')
            result = result.replace('V', 'Глагол')
            result = result.replace('P', 'Предлог')
            file.write(f'{sentence_list[i]}\n')
            file.write(f'{result}\n')

    file.close()
    end_loop = time.time()
    print('Время посчёта', end_loop - start_loop)
