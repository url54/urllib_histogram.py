# This is a program developed for py4e that uses urllib to 'GET' a text file
# from a web server, and then counts the words in that text file and returns a
# histogram of the data.

import urllib.request, urllib.parse, urllib.error

fhd = urllib.request.urlopen('http://data.pr4e.org/intro-short.txt')
ctr = dict()
for lne in fhd:
    wds = lne.decode().split()
    for wd in wds:
        ctr[wd] = ctr.get(wd, 0) + 1
print(ctr)
