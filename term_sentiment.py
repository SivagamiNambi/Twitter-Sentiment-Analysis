from __future__ import division
import sys
import json
from collections import defaultdict
def hw():
    print 'Hello, world!'

def lines(fp):
    print str(len(fp.readlines()))

def senti(file,scores):
    data=[]
    other_words=defaultdict(list)
    with open(file) as fp:
      for line in fp:
        data.append(json.loads(line))

    for i in range(0,len(open(file).readlines())):
      if 'created_at' in data[i].keys():
       sum=0
       a=data[i]['text'].split(' ')
       for word in a:
           if word.encode('utf-8') in scores.keys():
               sum+=scores[word.encode('utf-8')]
       for word in a:
           if word.encode('utf-8') not in scores.keys():
               other_words[word.encode('utf-8')].append(sum)

    for word in other_words:
        sum=0
        for value in other_words[word]:
            sum+=value
        print word,sum/len(other_words[word])




def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    scores={}
    for line in sent_file:
     term,score=line.split('\t')
     scores[term]=int(score)
    #print scores.items()
    senti(sys.argv[2],scores)


if __name__ == '__main__':
    main()
