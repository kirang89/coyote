#!/usr/bin/env Python
#-*- coding: utf8 -*-
#
# Crawler Script
#

import sys
import urllib2
import pylibmc


def get_links(url):
    urls = []
    content = urllib2.urlopen(url).read()
    while True:
        link = content.find('<a href=')
        if link != -1:
            squote = content.find('"', link)
            equote = content.find('"', squote + 1)
            urls.append(content[squote + 1:equote])
            content = content[equote:]
        else:
            break
    return urls


def crawl(target):
    crawled = []
    tocrawl = [target]
    for url in tocrawl:
        if url not in crawled:
            links = get_links(url)
            crawled.append(url)
            tocrawl.extend(links)

    #Initialising a memcached client
    try:
        mc = pylibmc.Client(['127.0.0.1'], binary=True)
        mc.behaviors = {"tcp_nodelay": True, "ketama": True}
        mc.set('urls_crawled', crawled)
    except Exception, e:
        print e

    return crawled

if __name__ == '__main__':
    from pprint import pprint
    url = sys.argv[1]
    cwurls = crawl(url)
    print "+++++++++++++++++"
    print "  Crawled URLs:  "
    print "+++++++++++++++++"
    pprint(cwurls)
