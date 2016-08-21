#!/usr/bin/env python
# f5do - lib: REST API Client
# https://github.com/ArtiomL/f5do
# Artiom Lichtenstein
# v0.1, 21/08/2016

import json
import requests

__author__ = 'Artiom Lichtenstein'
__license__ = 'MIT'
__version__ = '0.1'

class iControl(object):

	def __init__(self, strHost, strUser, strPasswd):
		self.host = strHost
		self.user = strUser
		self.passwd = strPasswd
		self.mburl = 'https://%s/mgmt/tm' % strHost

		self.objHSession = requests.session()
		self.objHSession.auth = (strUser, strPasswd)
		self.objHSession.verify = False
		self.objHSession.headers.update({ 'Content-Type': 'application/json' })


	def get(self, strURL):
		try:
			return self.objHSession.get(strURL).json()
		except Exception as e:
			return { 'Exception' : str(e) }


	def getPool(self, strPName = '', strPartition = '~Common~'):
		if not strPName:
			strPartition = ''
		return self.get('%s/ltm/pool/%s%s' % (self.mburl, strPartition, strPName))


	def getAddrList(self, strALName = '', strPartition = '~Common~'):
		if not strALName:
			strPartition = ''
		return self.get('%s/security/firewall/address-list/%s%s' % (self.mburl, strPartition, strALName))
