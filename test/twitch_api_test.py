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

  def test_get_user_id(self):
    user_id = self.api.get_user_id("lusciousdev")
    self.assertEqual(user_id, '82920215')
    
  def test_get_user_info(self):
    user_info : TwitchUser = self.api.get_user('82920215')
    self.assertEqual(user_info.login, 'lusciousdev')
    
  def test_get_clip(self):
    clip_id = "VictoriousStormyAsteriskKippa-BoS-i0TRLdP3bEO2"
    twitch_clip : TwitchClip = self.api.get_clip(clip_id)
    
    self.assertEqual(twitch_clip.clip_id, clip_id)
    self.assertEqual(twitch_clip.creator_name, "lusciousdev")
    self.assertEqual(twitch_clip.broadcaster_name, "itswill")
    
  def test_create_clip_response(self):
    create_clip_response : CreateClipResponse = CreateClipResponse({ "edit_url": "test url", "id": "test clip id" })
    
    self.assertEqual(create_clip_response.edit_url, "test url")
    self.assertEqual(create_clip_response.clip_id, "test clip id")
    
  def test_get_video(self):
    video_id = "396290251"
    twitch_video : TwitchVideo = self.api.get_video(video_id)
    
    self.assertEqual(twitch_video.video_id, video_id)
    self.assertEqual(twitch_video.title, "Emerald Nuzlocke Elite 4")
    self.assertEqual(twitch_video.user_name, "itswill")
    
  def test_get_channel_info(self):
    user_id : str = self.api.get_user_id("lusciousdev")
    channel_info : TwitchChannelInfo = self.api.get_channel_info(broadcaster_id = user_id)
    
    self.assertEqual(channel_info.broadcaster_id, user_id)
    self.assertEqual(channel_info.broadcaster_login, "lusciousdev")
    
  def test_get_category_info(self):
    game_name : str = "Old School RuneScape"
    category_info : TwitchCategoryInfo = self.api.get_category_by_name(game_name)
    
    self.assertEqual(category_info.category_id, '459931')
    self.assertEqual(category_info.name, game_name)
    
  def test_get_category_id(self):
    game_name : str = "Old School RuneScape"
    category_id : str = self.api.get_category_id(game_name)
    
    self.assertEqual(category_id, '459931')
    
  def test_get_global_emotes(self):
    emotes : typing.List[TwitchEmote]
    template : str
    emotes, template = self.api.get_global_emotes()
    
    self.assertTrue(len(emotes) > 0)
  
  def test_get_channel_emotes(self):
    user_id : str = self.api.get_user_id("itswill")
    emotes : typing.List[TwitchChannelEmote]
    template : str
    emotes, template = self.api.get_channel_emotes(user_id)
    
    self.assertTrue(len(emotes) > 0)
    
if __name__ == '__main__':
  unittest.main()