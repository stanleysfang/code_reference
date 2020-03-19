
#### Initialize Local Repository ####
repo_path=/home/sfang/windows/gitlab/stanleysfang/code_reference/ # code_reference repository will be used as an example

mkdir -p ${repo_path}
cd ${repo_path}
git init
touch README.md
cp /home/sfang/windows/gitlab/stanleysfang/code_reference/.gitignore . # copy a standard .gitignore file from code_reference repository
git add -A
git commit -m "initial commit"

#### Remote Repository ####
# Make sure to first create a blank repository on gitlab/github.
git remote add origin git@gitlab.com:stanleysfang/code_reference.git
git push origin master

git remote add github git@gitlab.com:stanleysfang/code_reference.git
git push github master
