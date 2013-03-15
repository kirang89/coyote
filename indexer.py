#!/usr/bin/env Python
#-*- coding: utf8 -*-
#
# The url indexer
#

import urllib2
import pylibmc
import sys


def filter(words):
    wordlist = []
    for word in words:
        if word.isalpha() and len(word) > 2:
            wordlist.append(word)
    return list(set(wordlist))


def index():
    try:
        mc = pylibmc.Client(['127.0.0.1'], binary=True)
        mc.behaviors = {"tcp_nodelay": True, "ketama": True}
        urls = mc.get('urls_crawled')
        if urls:
            for url in urls:
                page = urllib2.urlopen(url).read()
                words = page.split(' ')
                wordlist = filter(words)
                for word in wordlist:
                    urllist = mc.get(word)
                    if urllist and len(urllist) > 0:
                        urllist.append(url)
                        mc.set(word, urllist)
                    else:
                        mc.set(word, [url])
        print "Indexing Completed"
    except Exception, e:
        print e
        sys.exit(1)

if __name__ == '__main__':
    index()
