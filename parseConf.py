#! /usr/bin/env python3
def parse(fName):
    try:
        return parseFile(fName)
    except:
        raise SyntaxError('The config file is ineligible to me.')

def parseFile(fName):
    stdin = open(fName,'r')
    data = stdin.read().split('\n')
    result = {}
    for line in data:
        if bool(line.strip()) and line.strip()[0] != '#':
            kv = line.split('=')
            result[kv[0].strip()]=kv[1].strip()
    return result

if __name__ == '__main__':
    import sys
    print(parseFile(sys.argv[1]))
