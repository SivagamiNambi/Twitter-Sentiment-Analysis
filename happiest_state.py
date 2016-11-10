from __future__ import division
import sys
import json
from collections import defaultdict

def hw():
    print 'Hello, world!'

def lines(fp):
    print str(len(fp.readlines()))

def senti(file,scores):
    states = {
        'AK': 'Alaska',
        'AL': 'Alabama',
        'AR': 'Arkansas',
        'AS': 'American Samoa',
        'AZ': 'Arizona',
        'CA': 'California',
        'CO': 'Colorado',
        'CT': 'Connecticut',
        'DC': 'District of Columbia',
        'DE': 'Delaware',
        'FL': 'Florida',
        'GA': 'Georgia',
        'GU': 'Guam',
        'HI': 'Hawaii',
        'IA': 'Iowa',
        'ID': 'Idaho',
        'IL': 'Illinois',
        'IN': 'Indiana',
        'KS': 'Kansas',
        'KY': 'Kentucky',
        'LA': 'Louisiana',
        'MA': 'Massachusetts',
        'MD': 'Maryland',
        'ME': 'Maine',
        'MI': 'Michigan',
        'MN': 'Minnesota',
        'MO': 'Missouri',
        'MP': 'Northern Mariana Islands',
        'MS': 'Mississippi',
        'MT': 'Montana',
        'NA': 'National',
        'NC': 'North Carolina',
        'ND': 'North Dakota',
        'NE': 'Nebraska',
        'NH': 'New Hampshire',
        'NJ': 'New Jersey',
        'NM': 'New Mexico',
        'NV': 'Nevada',
        'NY': 'New York',
        'OH': 'Ohio',
        'OK': 'Oklahoma',
        'OR': 'Oregon',
        'PA': 'Pennsylvania',
        'PR': 'Puerto Rico',
        'RI': 'Rhode Island',
        'SC': 'South Carolina',
        'SD': 'South Dakota',
        'TN': 'Tennessee',
        'TX': 'Texas',
        'UT': 'Utah',
        'VA': 'Virginia',
        'VI': 'Virgin Islands',
        'VT': 'Vermont',
        'WA': 'Washington',
        'WI': 'Wisconsin',
        'WV': 'West Virginia',
        'WY': 'Wyoming'
    }
    data=[]

    with open(file) as fp:
      for line in fp:
        data.append(json.loads(line))
    happy=defaultdict(list)
    for i in range(0,len(open(file).readlines())):
      if 'created_at' in data[i].keys():
            sum=0
            a=data[i]['text'].split(' ')
            for word in a:
             if word.encode('utf-8') in scores.keys():
               sum+=scores[word.encode('utf-8')]
            # print str(sum)
             if 'place' in data[i].keys():
                 if data[i]['place']:
                  state= data[i]['place']['full_name'].split(', ')
                  if len(state) >1 :
                      if state[1] in states.keys():
                         happy[state[1]].append(sum)
    #print happy
    max=-100
    happy_state=' '
    for st in happy:
        sum=0
        for val in happy[st]:
            sum+=val;
        if( sum/len(happy[st]) > max):
          max=sum/len(happy[st])
          happy_state=st.encode('utf-8')
    print happy_state





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
