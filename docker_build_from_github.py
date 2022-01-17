from os import path
from git import Repo
import subprocess
import git
import sys

repo_path = "C:/Users/lava/lavadocker"
repository = Repo.init(repo_path)
AUTH="auth_creds for accesing nugget/packages/artifactory/libraries"
REGISTRY="Library/nugget/package management tool url"
branch = "test3"

repo = git.Repo(repo_path)
print("GIT init completed")

print("clone started")
#git.Git(repo_path).clone("https://github.com/xxxxxx.git")
print("clone completed")

print("checkout started")
repo.git.checkout(branch)
print("checkout completed")

print("pull started")
repo = git.Repo('C:/Users/lava/lavadocker')
origin = repo.remote(name='origin')
origin.pull()
print("pull completed")

#git.cmd.Git().pull('https://github.com/xxxxx.git','main') 
########## Clonning teh github repo ##########
# repo = git.Repo('/Users/lava/lavadocker')
# repo.remotes.upstream.pull('master')
#git.Repo.clone_from('https://github.com/xxxxxx.git', '/Users/lava/lavadocker')

#print("Clonned the repo from GitHub")
# Git Pull #

# repo = git.Repo('reactauth')
# origin = repo.remote(name='origin')
# origin.pull()

############## Docker image creation ####################
branch = "cd /Users/lava/lavadocker && git branch"
subprocess.call(branch, shell=True)

############## To Pass auth and registry as arguments ex: python3 gitclone.py <authtoken> <registry>/ ####################

# docker_build = "docker build --no-cache --build-arg ARTIFACTORY_AUTH="+sys.argv[1]+" --build-arg REGISTRY="+sys.argv[2]+" C:/Users/lava/lavadocker"

############## To build normal ################################
# docker_build = "docker build --no-cache C:/Users/lava/lavadocker"
# subprocess.call(docker_build, shell=True)

############## To Pass auth and registry as variables in python script ################################

docker_build = "docker build -t v1 --no-cache --build-arg ARTIFACTORY_AUTH="+AUTH+" --build-arg REGISTRY="+REGISTRY+" C:/Users/lava/lavadocker"
subprocess.call(docker_build, shell=True)

docker_images = "docker images"
subprocess.call(docker_images, shell=True)

docker_push = "docker push myregistry.azurecr.io/myimage:v1"
subprocess.call(docker_push, shell=True)
