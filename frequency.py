import sys
import json

def hw():
    print 'Hello, world!'

def lines(fp):
    print str(len(fp.readlines()))

def freq(file):
    data={}

    with open(file) as fp:
      for line in fp:
        if 'created_at' in json.loads(line).keys():
            a=json.loads(line)['text'].split()

            for word in a:
                if word.encode('utf-8') in data.keys():
                   data[word.encode('utf-8')]+=1;
                else:
                   data[word.encode('utf-8')]=1
    sum=0
    for key, value in data.iteritems() :
        sum=sum+value
    for key, value in data.iteritems() :
        print key,str(float(value)/sum)


def main():
    tweet_file = open(sys.argv[1])
    freq(sys.argv[1])


if __name__ == '__main__':
    main()
