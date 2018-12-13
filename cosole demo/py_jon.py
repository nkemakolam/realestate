from urllib import request,parse
url = 'https://api.github.com/users/nkemakolam'
params={
    'username' : 'nkemakolam',
    'password' : 'NKEMA@ghosts123'
}

headers = {
'User-agent' : 'none/ofyourbusiness',
'Spam' : 'Eggs'
}
querystring = parse.urlencode(params)
u = request.urlopen(url, querystring.encode('ascii'),headers=headers)
resp = u.read()
print(resp.text)