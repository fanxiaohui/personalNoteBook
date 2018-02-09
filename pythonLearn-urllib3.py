

#http://httpbin.org/ , provide HTTP Request & Response Service
#everyone could use this URL to test urllib3 API usage.
#help(urllib3.ProxyManager) to know the API


import certifi  #for https
import urllib3



if __name__ == '__main__':
    
    proxy = urllib3.ProxyManager(proxy_url = 'https://xx.xx.xx.xx:port',
                                 cert_reqs = 'CERT_REQUIRED',
                                 ca_certs  = certifi.where()
                                 )

    try:
        r = proxy.request('GET',
                          'https://www.google.fi',
                          retries = False,
                          timeout = 10.0)
        
    except urllib3.exceptions.NewConnectionError:
        print('connection failed')

    print(r.status, '\n', r.headers,'\n')
    
    if r.status  in [200, 302] : #200 = ok, 302 = redirection
        print('\n connect ok. \n')
    else:        
        print('\n connect error, status = ', r.status)
        
    
        

    

                                   

//////////////////////////////output:

200 
 HTTPHeaderDict({'Date': 'Fri, 09 Feb 2018 09:31:50 GMT', 'Expires': '-1', 'Cache-Control': 'private, max-age=0', 
                 'Content-Type': 'text/html; charset=ISO-8859-1', 'P3P': 'CP="This is not a P3P policy! 
                 See g.co/p3phelp for more info."', 'Server': 'gws', 'X-XSS-Protection': '1; mode=block', 
                 'X-Frame-Options': 'SAMEORIGIN', 'Set-Cookie': '1P_JAR=2018-02-09-09; expires=Sun, 11-Mar-2018 09:31:50 GMT; 
                 path=/; domain=.google.fi, NID=123=WrFxknbzRcoYbmB2xUBOa34RYrbfzx_A9-h3qOb79Iv_NxkgeiNVonpxu7EJDu9enpZYTb41gnCg7haEf-Qx9ZXd3QNkLnjneRE2Hv9lIW-hIR7M0FagaEzaWFmqOT0S; 
                 expires=Sat, 11-Aug-2018 09:31:50 GMT; path=/; domain=.google.fi; HttpOnly', 'Alt-Svc': 'hq=":443"; 
                 ma=2592000; quic=51303431; quic=51303339; quic=51303338; quic=51303337; 
                 quic=51303335,quic=":443"; ma=2592000; v="41,39,38,37,35"', 'Accept-Ranges': 'none', 'Vary': 'Accept-Encoding', 'Transfer-Encoding': 'chunked'}) 


 connect ok. 
