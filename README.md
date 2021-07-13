# README

## branches
origin  ssh://entolusis@mattnas2:/volume1/git/matt.com.git (fetch)
origin  ssh://entolusis@mattnas2:/volume1/git/matt.com.git (push)


## deployment
add a tag before copying to remote server

git tag -a v1.1 -m "v1.1 deployed on 2020/03/06"

scp -rp  ./matt.com/[!.]* matt.com:/var/www/matthieuchevrier.com