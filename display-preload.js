// under collection's Display tab, create a "scriptable section for advanced customisation"
// and then paste this into the lower Pre-load Javascript panel
var uuid = currentItem.getUuid()
var hash = currentItem.getUuid().hashCode() & 127
var version = currentItem.getVersion()
// beginning is the path to our filestore
var filestore = "/mnt/equelladata01/Institutions/cca2012/Attachments/" + hash + "/" + uuid + "/" + version
var stagingdir = '/mnt/equelladata01/' + xml.get('local/stagingDir')
// convert list-thing into JS array
var stagingList = xml.list('local/staging')
var staging = []
for (var i = 0; i < stagingList.size(); i++) {
    staging.push(stagingList.get(i))
}

// if item was created before we recorded staging files, skip the check script
if (staging.length > 0) {
    var params = [uuid, version, filestore, stagingdir].concat(staging)
    var cmd = '/Users/ephetteplace/staging-persistent-check.py ' + params.join(' ')

    logger.log('Running command: ' + cmd)
    system.executeInBackground('/Users/ephetteplace/staging-persistent-check.py', params)
}
