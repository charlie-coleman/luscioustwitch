import sys
sys.path.append('../')
from src.luscioustwitch import *
from src.luscioustwitch.events import *
import json

cred_json = json.load(open('../secrets.json', 'r'))
api = TwitchAPI(cred_json['TWITCH'])

user_id = api.get_user_id()
print(f'User ID: {user_id}')

api.setup_websocket() # "ws://localhost:8181/eventsub")

api.subscribe_to_follows(user_id,  lambda _, msg: print('New follower!'))

while True:
  time.sleep(1)