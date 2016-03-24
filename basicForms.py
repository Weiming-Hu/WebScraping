import requests
from requests.auth import AuthBase
from requests.auth import HTTPBasicAuth

def submitForm():
    params = {'firstname':"Ryan", 'lastname':"Mitchell"}
    r = requests.post("http://pythonscraping.com/pages/files/processing.php", data=params)
    print(r.text)
    
def submitFile():
    files = {"uploadFile":open('E:\lena.gif', 'rb')}
    r = requests.post("http://pythonscraping.com/files/processing2.php", files=files)
    print(r.text)

def loggin():
    session = requests.Session()
    
    params = {'username':'username', 'password':'password'}
    s = session.post("http://pythonscraping.com/pages/cookies/welcome.php", params)
    print("Cookie is set to: ")
    print(s.cookies.get_dict())
    print("-" * 10)
    print("Going to profile page...")
    s = session.get("http://pythonscraping.com/pages/cookies/profile.php")
    print(s.text)
    
def logginAuth():
    auth = HTTPBasicAuth('ryan', 'password')
    r = requests.post(url='http://pythonscraping.com/pages/auth/login.php', auth=auth)
    print(r.text)
    

if __name__ == '__main__':
#     submitForm()
#     submitFile()
#     loggin()
    logginAuth()