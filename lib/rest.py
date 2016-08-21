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
		self.murl = 'https://%s/mgmt/tm' % strHost

		self.objSession = requests.session()
		self.objSession.auth = (strUser, strPasswd)
		self.objSession.verify = False
		self.objSession.headers.update({ 'Content-Type': 'application/json' })

	def getPool(self, strPName = '', strPartition = '~Common~'):
		if not strPName:
			strPartition = ''
		strURL = '%s/ltm/pool/%s%s' % (self.murl, strPartition, strPName)
		req = self.objSession.get(strURL)
		return req.json()

	def getAddrList(self, strALName = '', strPartition = '~Common~'):
		if not strALName:
			strPartition = ''
		strURL = '%s/security/firewall/address-list/%s%s' % (self.murl, strPartition, strALName)
		req = self.objSession.get(strURL)
		return req.json()
