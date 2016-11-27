#!/usr/bin/env python
# f5do - lib: Logging
# https://github.com/ArtiomL/f5do
# Artiom Lichtenstein
# v1.0.0, 08/11/2016

import subprocess
import time

__author__ = 'Artiom Lichtenstein'
__license__ = 'MIT'
__version__ = '1.0.0'

# Log level to /var/log/ltm (or stdout)
intLogLevel = 0
strLogMethod = 'log'
strLogID = '[-v%s-161108-] - ' % __version__

# Logger command
strLogger = 'logger -p local0.'

def funLog(intMesLevel, strMessage, strSeverity = 'info'):
	if intLogLevel >= intMesLevel:
		if strLogMethod == 'stdout':
			print('%s %s' % (time.strftime('%b %d %X'), strMessage))
		else:
			lstCmd = (strLogger + strSeverity).split(' ')
			lstCmd.append(strLogID + strMessage)
			subprocess.call(lstCmd)
