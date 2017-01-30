# -*- coding: utf-8 -*-
from urllib import request
from pyquery import PyQuery as pq
import time

base_url = 'http://yukicoder.me'

names = [
    ['threepipes_s', 137],
#    ['kyuridenamida', 236],
    ['a3636tako', 2228],
#    ['tatsukawa_', 983],
    ['crazybbb3', 2658],
    ['astatine0x55', 2764],
    ['sntea', 995],
    ['frnfnts', 2229],
    ['37', 2068],
]

problems = [
    299, 144, 130, 101,
]
ranking = {}
for name in names:
    ranking[name[0]] = {}
    for prob in problems:
        ranking[name[0]][prob] = '-'


part = '-'*15
for prob in problems:
        part += str(prob) + '\t'
def printRanking():
    print('\n'*10)
    print(part)
    for name in names:
        line = name[0] + ' '*(15-len(name[0]))
        for prob in problems:
            line += ranking[name[0]][prob] + '\t'
        print(line)

printRanking()

while True:
    change = False
    for name in names:
        query = pq(base_url+'/users/%d/submissions' % name[1], parser='html')
        acList = []
        no = ""
        for submission in query.find('tr'):
            sq = pq(submission)
            if sq.attr('class') != '':
                continue
            for item in sq.find('td'):
                txt = pq(item).text().split(' ')[0]
                if 'No.' in txt:
                    no = int(txt.split('.')[1])
                elif 'AC' in txt:
                    acList.append(no)
        for prob in problems:
            if prob in acList and ranking[name[0]][prob] == '-':
                change = True
                ranking[name[0]][prob] = 'o'
        time.sleep(5)
    if change:
        printRanking()
    time.sleep(2)
