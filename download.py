import geturls
import sys

import argparse

parser = argparse.ArgumentParser('Download tumblr artist images in raw size')
parser.add_argument('-a', help='artist name, <name>.tumblr.com')
parser.add_argument('-d', help='directory to save files')

if __name__ == '__main__':
    args = parser.parse_args()
    artist = args.a
    urls = geturls.get_urls(artist, 0)