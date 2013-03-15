#!/usr/bin/env Python
#-*- coding: utf8 -*-
#
# The coyote-ish searcher
#

import pylibmc
import sys


def search(queryAsList):
    result = []
    words = list(set(queryAsList))
    mc = pylibmc.Client(['127.0.0.1'], binary=True)
    mc.behaviors = {"tcp_nodelay": True, "ketama": True}
    for word in words:
        urls = mc.get(word)
        if urls:
            result.extend(urls)
    print "++++++++++++++"
    print "Search Results"
    print "++++++++++++++"
    if len(result) > 0:
        for index, url in enumerate(list(set(result))):
            print "{0}. {1}".format(index, url)
    else:
        print "No results found"

if __name__ == '__main__':
    if len(sys.argv) > 1:
        query = sys.argv[1:]
        search(query)
    else:
        print "No query entered"
