#! data/data/com.termux/files/usr/bin/python
# coded by @ciku370

import requests
import bs4
import sys

num = 20 # the number of proxies you want to make

class table:
    def __init__(self,data):
        self.RESULTS = data['contents']
        self.TITLE = data['title']
        self.get_long_word()

    def get_long_word(self):
        self.MAX_ALL = {i:len(i) for i in self.TITLE}
        for i in range(0,len(self.RESULTS)):
            for _ in self.TITLE:
                if len(self.RESULTS[i][_]) >= self.MAX_ALL[_]:
                    self.MAX_ALL[_] = len(self.RESULTS[i][_])
        self.create_table()
    def header_footer(self):
        for i in self.TITLE:
            sys.stdout.write((self.MAX_ALL[i]+2)*'-'+'+')
    def create_table(self):
        sys.stdout.write('\n +')
        self.header_footer()
        sys.stdout.write('\n |')
        for i in self.TITLE:
            sys.stdout.write(i.center(self.MAX_ALL[i]+2)+'|')
        sys.stdout.write('\n +')
        self.header_footer()
        print ('')
        for x in range(0,len(self.RESULTS)):
            sys.stdout.write(' |')
            for i in self.TITLE:
                sys.stdout.write(' '+self.RESULTS[x][i]+((self.MAX_ALL[i]-len(self.RESULTS[x][i])+1)*' ')+'|')
            print ('')
        sys.stdout.write(' +')
        self.header_footer()
        print ('\n')

class proxy:
    def __init__(self):
        self.text = requests.get('https://free-proxy-list.net').text
        self.soup = bs4.BeautifulSoup(self.text,'html.parser')

    def get(self,numbers=20):
        data = { 'title':[], 'contents':[] }
        for num,contents in enumerate(self.soup.find_all("tr")):
            if len(data['contents']) != numbers:
                if num == 0:
                    for t in contents.find_all('th'):
                        data['title'].append(t.text)
                else:
                    temp = {}
                    for num,x in enumerate(contents.find_all('td')):
                        temp[data['title'][num]] = x.text
                    if len(temp) == len(data['title']):
                        data['contents'].append(temp)
            else:
                break
        return data

table(proxy().get(num))
