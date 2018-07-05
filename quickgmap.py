#!/usr/bin/env python
# -*- coding: utf-8 -*-
import urllib2
import sys
import os
import platform
import webbrowser

def main():
    if len(sys.argv) == 1:
        print("Try qgmap 緯度latitude,經度longitude || qgmap 緯度latitude 經度longitude")
        return
    if len(sys.argv) == 3:
        url = "http://maps.google.com/?q=" + sys.argv[1] + "," + sys.argv[2]
        webbrowser.open(url)
        return
    query = " ".join(sys.argv[1:])
    url = "http://maps.google.com/?q=" + query
    webbrowser.open(url)

if __name__ == '__main__':
    main()
