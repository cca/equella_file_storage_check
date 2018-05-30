#!/usr/bin/env python
# python 2 script, default version on our ubuntu is 2.7.6
"""
Usage: ./staging-persistent-check.py $ITEM_UUID $ITEM_VERSION $FILE_STORAGE_DIR $STAGING_FILE_1 $STAGING_FILE_2 ...

Any number of positional staging files can be passed after the persistent file storage directory. This script will check the passed staging files against the contents of the persistent file storage, ignoring a few EQUELLA-generated directories (_uploads, _THUMBS, _VIDEOPREVIEW). It logs both directory listings to a hard-coded log file /Users/ephetteplace/logs/log.txt and then, if there are staging files that are not in the persistent file storage, sends an email to ephetteplace@cca.edu and vault@cca.edu with details.
"""
import datetime
import os
import re
import smtplib
import sys
import time

uuid = sys.argv[1]
version = sys.argv[2]
persistent_path = sys.argv[3]
url = 'https://vault.cca.edu/items/%s/%s/' % (uuid, version)

# long story...due to annoying limitations with passing JSON around
# all the staging files are passed as positional arguments after the first 3
# parameters so we need to gather them up into a list
staging_files = sys.argv[4:]

# test which skips EQUELLA-generated directories
def isRealFile(str):
    if not re.match("^_uploads", str) and not re.match("^_THUMBS", str) and not re.match("^_VIDEOPREVIEW", str):
        return True
    else:
        return False

staging_files = set([f for f in staging_files if isRealFile(f)])

# wait for staging files to be copied into persistent directory
# this only matters on new item creation not repeated viewings
time.sleep(1)

persistent_files = os.listdir(persistent_path)
persistent_files = set([f for f in persistent_files if isRealFile(f)])
files_are_missing = not persistent_files.issubset(staging_files)

logfile = '/Users/ephetteplace/logs/log.txt'
with open(logfile, 'a') as log:
    log.write(str(datetime.datetime.now()) + '\t')
    log.write('Item: ' + url + '\t')
    log.write('Staging: [' + ', '.join(staging_files) + ']\t')
    log.write('Persistent: [' + ', '.join(persistent_files) + ']\t')
    log.write('Files missing: ' + str(files_are_missing) + '\n')
    log.close()

if files_are_missing:
    from_adr = 'From: VAULT <vault@cca.edu>'
    to_adrs = ['Eric Phettplace <ephetteplace@cca.edu>', 'VAULT <vault@cca.edu>']
    msg = """\
From: %s
Reply-To: noreply@cca.edu
To: %s
Subject: EQUELLA Disappearing Files

Item %s has discrepancies between staging & persistent files.

Staging files:
        - %s

Persistent storage:
        - %s

""" % (from_adr, ', '.join(to_adrs), url, '\n\t- '.join(staging_files), '\n\t- '.join(persistent_files))

    server = smtplib.SMTP('localhost')
    server.sendmail(from_adr, to_adrs, msg)
    server.quit()
