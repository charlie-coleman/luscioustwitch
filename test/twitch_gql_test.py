import sys
sys.path.append('../')
from src.luscioustwitch import *
import json
import unittest

class TestGqlAPI(unittest.TestCase):
  @classmethod
  def setUpClass(self):
    self.gql = TwitchGQL_API()
    
  def test_get_clip(self):
    clip_id = "PlainFurryRaisinBrokeBack-7bzdbBoHeUT6XupJ"
    clip = self.gql.get_clip(clip_id)
    
    self.assertEqual(clip.clipId, '2382936331')
    self.assertEqual(clip.playbackAccessToken.value["clip_slug"], clip_id)
    
  def test_get_video(self):
    video_id = "2383314291"
    video = self.gql.get_video(video_id)
    
    self.assertEqual(video.videoId, video_id)
    self.assertEqual(video.owner["displayName"], "itswill")
    
if __name__ == '__main__':
  unittest.main()