#! /usr/bin/env python3
import sys
import urllibRequests as ur
import datetime
import time
import xml.etree.ElementTree as ET
import parseConf
import version

def main():
    conf = parseConf.parse('weather.conf')
    data = {
'whichClient':'NDFDgenMultiZipCode',
'zipCodeList':conf['zipCode'],
'product':'glance',
'begin':datetime.datetime.fromtimestamp(int(time.time())).isoformat(),
'end':(datetime.datetime.fromtimestamp(int(time.time()))+datetime.timedelta(0.5)).isoformat(),
'Unit':'e',
'icons':'icons',
'Submit':'Submit'}
    req = ur.get('http://graphical.weather.gov/xml/SOAP_server/ndfdXMLclient.php',data)
    tree = ET.fromstring(req.text)
    info = tree.find('data').find('parameters').find('conditions-icon').find('icon-link')
    print(info.text[39:-4])

if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] in ['-v','--version']:
        version.printVersion()
    else:
        main()
