#!/bin/bash

mkdocs build --clean

git checkout gh-pages
[ $? != 0 ] && exit 1
git rm -rf .
mv site/* .
rmdir site/

git add -A
git commit -m 'update site'
git push origin gh-pages

git checkout master
