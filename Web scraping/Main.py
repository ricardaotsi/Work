import requests

# Fill in your details here to be posted to the login form.
payload = {
    'login': 'ricardo.arruda',
    'senha': 'ricardogoogle'
}

# Use 'with' to ensure the session context is closed after use.
with requests.Session() as s:
    p = s.post('https://sipac.ifpr.edu.br/sipac/logon.do', data=payload)
    # print the html returned or something more intelligent to see if it's a successful login page.
    #print(p.text)

    # An authorised request.
    r = s.get('https://sipac.ifpr.edu.br/sipac/portal_administrativo/index.jsf')
    print(r.text)
        # etc...
