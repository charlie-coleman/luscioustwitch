import sys
sys.path.append('../')
from src.luscioustwitch import *
from luscioustwitch.lushevents import *
import json

cred_json = json.load(open('../secrets.json', 'r'))
lushapi = TwitchAPI(cred_json['TWITCH'])

user_id = lushapi.get_user_id()
print(f'User ID: {user_id}')

lushapi.setup_websocket() # "ws://localhost:8181/eventsub")

lushapi.subscribe_to_follows(user_id,  lambda _, msg: print('New follower!'))

while True:
  time.sleep(1)