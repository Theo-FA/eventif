from django.test import TestCase

class SpeakerDetailGet(TestCase) :
  def test_get(self):
    resp = self.client.get('/palestrantes/grace-hopper/')
    self.assertEqual(200, resp.status_code)