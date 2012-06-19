# -*- coding: utf-8 -*-

import requests

SLUG = "%s/%s"
REPOS = "http://travis-ci.org/repositories.json"
REPO = "http://travis-ci.org/%s/%s.json"
BUILDS = "http://travis-ci.org/%s/builds.json"
BUILD = "http://travis-ci.org/%s/%s/%s.json"

class Cute(object):
    """
        Base class to create objects from request().json
    """
    def __init__(self, d):
        for k,v in d.items():
            if type(v) == type(dict):
                setattr(self, k, Cute(v)) # cute dictionaries
            elif type(v) == type(list):
                setattr(self, k, [Cute(x) for x in v]) # cute lists
            else:
                setattr(self, k, v)

class Repo(Cute):
    """
        The representation of a repository
    """
    @property
    def builds(self):
        return get_builds(self.slug)
    
    @property
    def last(self):
        return self.builds[-1]
    
    @property
    def stable(self):
        return not self.last.result


class  Build(Cute):
    """
        The representation of a Build()
    """
    @property
    def passed(self):
        return not self.result
    

def repositories():
    """
        A list of Repo()s
    """
    r = request(REPOS)
    repos=list()
    for repo in r.json:
        repos.append(Repo(repo))
    return repos

def show(owner, repo, build=None):
    """
        Returns a Repo()or build depending on what you want
    """
    if build:
        return Build(request(BUILD % (owner, repo, build)).json)
    else:
        return Repo(request(REPO % (owner, repo)).json)

def builds(owner, repo):
    """
        A list of Build()s
    """
    return get_builds('%s/%s' % (owner, repo))

def get_builds(slug):
    r = request(BUILDS % slug)
    builds=list()
    for build in r.json:
        builds.append(Build(build))
    return builds

def request(url):
    """
        Returns a request object with some parameters set for all requests
    """
    r = requests.get(url, allow_redirects=False)
    if r.ok:
        return r
    else:
        # RAISE HELL
        pass


#ks=list(show('medecau', 'worm').last.__dict__)
#ks.sort()
#for k in ks:
#    print k
#print repositories()
print show('travis-ci', 'travis-ci', 9)
