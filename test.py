import urllib2

proxy = urllib2.ProxyHandler({'http': 'http://test:test@127.0.0.1:3128'})
auth = urllib2.HTTPBasicAuthHandler()
opener = urllib2.build_opener(proxy, auth, urllib2.HTTPHandler)
urllib2.install_opener(opener)

conn = urllib2.urlopen('http://python.org')
return_str = conn.read()
