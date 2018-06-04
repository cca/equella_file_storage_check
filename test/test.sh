#!/usr/bin/env fish
set storage (pwd)/test
set log ~/logs/log.txt
# clean out log file
echo -n '' > $log
echo 'Attempting positive test (files match)'
# this UUID & version are just to a random VAULT item
python staging-persistent-check.py 4eb14fb4-1b10-4527-914c-85610df0fb61 1 $storage test.sh file.jpg
echo 'Attempting negative test (files mismatched)'
python staging-persistent-check.py 4eb14fb4-1b10-4527-914c-85610df0fb61 1 $storage test.sh file.jpg doesnotexist.txt
echo
echo 'Contents of log file:'
cat $log
