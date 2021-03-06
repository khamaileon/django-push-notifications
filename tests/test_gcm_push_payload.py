import mock
from django.test import TestCase
from push_notifications.gcm import gcm_send_message, gcm_send_bulk_message


class GCMPushPayloadTest(TestCase):
	def test_push_payload(self):
		with mock.patch("push_notifications.gcm._gcm_send") as p:
			gcm_send_message("abc", {"message": "Hello world"})
			p.assert_called_once_with(
				"registration_id=abc&data.message=Hello+world",
				"application/x-www-form-urlencoded;charset=UTF-8")

	def test_bulk_push_payload(self):
		with mock.patch("push_notifications.gcm._gcm_send") as p:
			gcm_send_bulk_message(["abc", "123"], {"message": "Hello world"})
			p.assert_called_once_with(
				'{"data":{"message":"Hello world"},"registration_ids":["abc","123"]}',
				"application/json")
