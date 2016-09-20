#! /usr/bin/env python3
import sys

def main(args):
    data = args[0].split('&')
    for item in data:
        print('"'+item.replace('=','" : "')+'",')

if __name__ == '__main__':
    main(sys.argv[1:])
