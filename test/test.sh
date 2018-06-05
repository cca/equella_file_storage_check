#!/usr/bin/env fish
set storage (pwd)/test/storage
set staging (pwd)/test/staging
# this UUID is just a random VAULT item
set uuid 4eb14fb4-1b10-4527-914c-85610df0fb61
set logdir ~/logs
set log $logdir/log.txt
# clean out log directory then recreate log file
rm -rf $logdir; and mkdir -p $logdir; and touch $log
echo 'Attempting positive test (files match)'
python staging-persistent-check.py $uuid 1 $storage $staging file.txt file.jpg
echo 'Attempting negative test (files mismatched)'
python staging-persistent-check.py $uuid 1 $storage $staging file.txt file.jpg doesnotexist.txt
echo 'You should receive an email from this second test.'
echo -e '\nContents of log file:'
cat $log
echo -e '\nContents of backup directory:'
ls -l $logdir/$uuid/1
