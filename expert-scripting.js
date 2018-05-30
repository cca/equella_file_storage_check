// place at the bottom of a collection's Expert Scripting > Save Script
// used to check if an item's staging directory contains the same files as its
// persistent storage does, use staging API
if (staging.isAvailable()) {
    xml.deleteAll('local/staging') // clear out previous results
    var stagingFilesAndDirs = staging.listFiles("", "**")
	for(var i = 0; i < stagingFilesAndDirs.size(); i++) {
		xml.add('local/staging', stagingFilesAndDirs.get(i))
	}
}
