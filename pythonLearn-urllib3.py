

#http://httpbin.org/ , provide HTTP Request & Response Service
#everyone could use this URL to test urllib3 API usage.

import certifi   #this is needed when visit https://xxx
import urllib3

#http = urllib3.PoolManager(cert_reqs='CERT_REQUIRED', ca_certs=certifi.where())

if __name__ == '__main__':
    proxy = urllib3.ProxyManager('http://xx.xx.xx.xx:port')

    try:
        r = proxy.request('GET', 'http://www.baidu.com',retries=False, timeout = 10.0)        
        
    except urllib3.exceptions.NewConnectionError:
        print('connection failed')

    print(r.status, '\n', r.headers,'\n')    
    print('main ok ')
        
    
        

    

        
    
        

//////////////////////////////output:

200 
 HTTPHeaderDict({'Date': 'Fri, 09 Feb 2018 06:31:04 GMT', 'Content-Type': 'text/html', 'Content-Length': '14615', 
 'Last-Modified': 'Tue, 06 Feb 2018 08:39:00 GMT', 'Vary': 'Accept-Encoding', 
 'Set-Cookie': 'BAIDUID=C4A3D22A850A7F2599042851F1C4C86E:FG=1; expires=Thu, 31-Dec-37 23:55:55 GMT; 
 max-age=2147483647; path=/; domain=.baidu.com, BIDUPSID=C4A3D22A850A7F2599042851F1C4C86E; 
 expires=Thu, 31-Dec-37 23:55:55 GMT; max-age=2147483647; path=/; domain=.baidu.com, PSTM=1518157864; 
 expires=Thu, 31-Dec-37 23:55:55 GMT; max-age=2147483647; path=/; domain=.baidu.com', 
 'P3P': 'CP=" OTI DSP COR IVA OUR IND COM "', 'X-UA-Compatible': 'IE=Edge,chrome=1', 'Server': 'BWS/1.1', 
 'Pragma': 'no-cache', 'Cache-control': 'no-cache', 'Accept-Ranges': 'bytes', 'Via': '1.1 fihel1d-proxy.emea.nsn-net.net'}) 

main ok 
