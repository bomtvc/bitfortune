import requests
from bs4 import BeautifulSoup
import os
from time import sleep

os.system('cls')

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'
}

data = {
 'PHPSESSID': '7a5872ecf30c645bfb6e01e3886ef07d'
}

claim_id = {
    'operation': 'allowSpin',
    'u_id': '10046'
}

POST_LOGIN_URL = 'https://bitfortune.club/member/lWk3CI7ML'
# REQUEST_URL = 'https://bitfortune.club/member/lWk3CI7ML'
SPIN_URL = 'https://bitfortune.club/domember.php'
s = requests.Session()
r = s.get(POST_LOGIN_URL)

def login():
    post = s.post(POST_LOGIN_URL, headers=headers, cookies=data)
    soup = BeautifulSoup(r.content, 'lxml')
    user = soup.select('h1')[0].text.strip()
    balance = soup.select('h3')[0].text.strip()
    oxygen = soup.select('span', id='oxygen')[1].text.strip()
    print('Hello', user)
    print('Balance: ', balance)
    print('Spins Available', oxygen)

def spin_click():
    post1 = s.post(SPIN_URL, headers=headers, cookies=data, data=claim_id)
    print('success: ', post1.content)

login()
spin_click()