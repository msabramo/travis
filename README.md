# travis

travis is Travis-CI service api wrapper for python


## Usage:

	import travis

	print show('travis-ci', 'travis-ci').last.stable


## Documentation:

### **repositories()**
list of the latest repos being tested

### **show(owner, repo, build=None)**
returns either a repository object
if a build number is provided then a build object is returned

### **builds(owner, repo)**
returns a list of builds for a given repo

### **get_builds()**
*meant for internal use*
works like **builds()**

### **Repo(dict())**

* description
* id
* last_build_duration
* last_build_finished_at
* last_build_id
* last_build_language
* last_build_number
* last_build_result
* last_build_started_at
* last_build_status
* public_key
* slug
* builds
* last
* stable


### **Build(dict())**

* branch
* commit
* duration
* event_type
* finished_at
* id
* message
* number
* repository_id
* result
* started_at
* state
* passed

### **Cute(dict())**
*meant for internal use*
both Repo() and Build() are based on this class
it receives a dict and makes all the keys available as attributes


## Bugs & Co.

If you find bugs or new features that are not implemented you can:

 * Fork and implement the changes
 * Fork and write a test that fails but shouldn't
 * Submit an issue in github


## Aknowledgment

Kenneth Reitz for being awesome and showing how to do things right
