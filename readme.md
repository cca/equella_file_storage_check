# EQUELLA Persistent vs Staging Files Check

This suite of scripts attempts to check if the files uploaded by a user and stored in a temporary staging directory during item creation are successfully moved to long-term file storage by the application.

Setup:

1. upload the staging-persistent-check.py script to each of your app nodes
2. create a logs directory with a "log.txt" file on each of your app nodes
3. add the contents of expert-scripting.js to the bottom of a collection's Expert Scripting Save Script
4. create a display ASC with the contents of display-preload.js in its Pre-load Javascript panel
5. repeat steps 4 & 5 for every collection you want to monitor

There are hard-coded directories littered throughout these scripts because I just wanted to get them working. Anyone trying to reuse them will need to remove the references to CCA and ephetteplace throughout.

# Notes

I tried for a long time to write this as an expert save script so that all the code could be in one place. The issue is that, for an item version in the process of being created (not even necessarily the first version, just any new version), files haven't been copied into the versioned persistent storage directory yet so there's no way to check them against staging.

I tried for a long time to pass the staging files to the script as JSON but it was impossible to figure out how to encode it correctly. EQUELLA doesn't provide access to the JSON utility in its server-side Rhino scripts so you can't do something as simple as `JSON.stringify()` the list of staging files and pass that. I even tried writing a primitive stringify function myself but it was still passing invalid JSON.

The staging files are eventually erased by EQUELLA, within a day it seems, so storing _what they used to be_ in the item's XML appears to be the best means of checking.

# LICENSE

[ECL Version 2.0](https://opensource.org/licenses/ECL-2.0)

Except for the included "file-lister-save-script.js" from Apereo which follows the license referred to in its frontmatter.
