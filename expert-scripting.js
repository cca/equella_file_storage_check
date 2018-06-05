// place at the bottom of a collection's Expert Scripting > Save Script
// used to check if an item's staging directory contains the same files as its
// persistent storage does, use staging API
if (staging.isAvailable()) {
    // clear out previous results
    xml.deleteAll('local/staging')
    xml.deleteAll('local/stagingDir')

    var stagingFilesAndDirs = staging.listFiles("", "**")
	for (var i = 0; i < stagingFilesAndDirs.size(); i++) {
		xml.add('local/staging', stagingFilesAndDirs.get(i))
	}

    var stagingFiles = staging.list("/", "*")
    if (stagingFiles.size() > 0) {
        // getHandle is technically unsupported but it works
        xml.add('local/stagingDir', staging.getFileHandle(stagingFiles.get(0)).getHandle().getAbsolutePath())
    }
}
