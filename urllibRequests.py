import urllib.request
import urllib.parse
import version
class Response:
    def __init__(self,data,charset='UTF-8'):
        self.text = data.decode(charset)

def getEncoding(ctstr):
    return ctstr[ctstr.find('charset')+8:]

def gunzip(data):
    import gzip
    return gzip.decompress(data)

def inflate(data):
    import zlib
    try:
        return zlib.decompress(data)
    except zlib.error:
        return zlib.decompress(data,-zlib.MAX_WBITS)

def get(urlStr,params={}):
    if params != {}:
        reqdata = urllib.request.Request(urlStr+'?'+urllib.parse.urlencode(params),method="GET")
    else:
        reqdata = urllib.request.Request(urlStr,method="GET")
    reqdata.add_header('User-Agent',
                       'WeatherGetter/'+version.strVersion()+' (https://github.com/StephDC/WeatherGetter)')
    reqdata.add_header('Accept-Encoding','gzip, deflate')
    req = urllib.request.urlopen(reqdata)
    if req.headers.get('Content-Encoding') is not None:
        if req.headers.get('Content-Encoding') == 'gzip':
            result = gunzip(req.read())
        elif req.headers.get('Content-Encoding') == 'deflate':
            result = inflate(req.read())
        else:
            result = req.read()
    else:
        result = req.read()
    if (req.headers.get('Content-Type') is not None and
        req.headers.get('Content-Type').find('charset') != -1):
        return Response(result,getEncoding(req.headers.get('Content-Type')))
    else:
        return Response(result)
