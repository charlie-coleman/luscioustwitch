import sys
sys.path.append('../')
from src.luscioustwitch import *
import json
import unittest

class TestTwitchAPI(unittest.TestCase):
  @classmethod
  def setUpClass(self):
    with open('../secrets.json', 'r') as f:
      cred_json = json.load(f)
      f.close()
    self.api = TwitchAPI({ "CLIENT_ID": cred_json['TWITCH']["CLIENT_ID"], "CLIENT_SECRET": cred_json['TWITCH']['CLIENT_SECRET'] })
    self.gql = TwitchGQL_API()
    
    print(self.api.DEFAULT_HEADERS)

  def test_get_user_id(self):
    user_id = self.api.get_user_id("lusciousdev")
    self.assertEqual(user_id, '82920215')
    
  def test_get_user_info(self):
    user_info = self.api.get_user_info('82920215')
    self.assertEqual(user_info['login'], 'lusciousdev')
    
  def test_get_channel_info(self):
    user_id = self.api.get_user_id("lusciousdev")
    channel_info = self.api.get_channel_info(user_id = user_id)
    
    self.assertEqual(channel_info['broadcaster_id'], user_id)
    self.assertEqual(channel_info['broadcaster_login'], "lusciousdev")
    
  def test_get_category_info(self):
    game_name = "Old School RuneScape"
    category_info = self.api.get_category_info(game_name)
    
    self.assertEqual(category_info['id'], '459931')
    self.assertEqual(category_info['name'], game_name)
    
  def test_get_category_id(self):
    game_name = "Old School RuneScape"
    category_id = self.api.get_category_id(game_name)
    
    self.assertEqual(category_id, '459931')
    
  def test_get_clip(self):
    clip_id = 'IgnorantEnergeticBananaHotPokket-9Rg1MRwc97VXfSzr'
    clip_info = self.api.get_clip(clip_id)
    
    self.assertEqual(clip_info['id'], clip_id)
    
if __name__ == '__main__':
  unittest.main()