import sys
sys.path.append('../')
from src.luscioustwitch import *
from luscioustwitch.lushevents import *
import json
import requests
import urllib.parse

api_url = 'http://localhost:8888/mock'
oauth_url = 'http://localhost:8888/auth/authorize'

client_id = '12f7c3311539c97e44cc9949e8a9c7'
client_secret = 'e2a2f5a794f4c84d0c79899921b452'

user_id = '11922382'

params = {
  'client_id': client_id,
  'client_secret': client_secret,
  'grant_type': 'user_token',
  'user_id': user_id,
  'scope': 'channel:read:redemptions channel:manage:redemptions'
}

r = requests.post(url = f'{oauth_url}?{urllib.parse.urlencode(params)}')

print(r.json())