# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.test import APIRequestFactory

# Create your tests here.

class InstallTestCase(APITestCase):
	def install_fetch(self):
		self.assertEqual(1, 1)