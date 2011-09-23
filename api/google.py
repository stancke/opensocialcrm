import json
import urllib
import urllib2
from urllib2 import HTTPError

class Google:

    def encurtaUrl(self,url):
    
        gurl = 'http://goo.gl/api/url?url=%s' % urllib.quote(url)
        req = urllib2.Request(gurl, data='')
        req.add_header('User-Agent', 'toolbar')
        results = json.load(urllib2.urlopen(req))
        return results['short_url']
    
    def analisar_dados(self, url):
        
        gurl = 'https://www.googleapis.com/urlshortener/v1/url?shortUrl=%s&projection=FULL' % urllib.quote(url)
        req = urllib2.Request(gurl)
        req.add_header('User-Agent', 'toolbar')
        try:
            results = json.load(urllib2.urlopen(req))
        except HTTPError, e:
            return e.read()
            
        return results

