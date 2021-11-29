#!usr/bin/env sh

set -e

npm run build

cd dist

git init
git add -A
git commit -m "Nouveau deploiement"
git push -f git@github.com:bastiansmn/portfolio-09-21.git master:gh-pages

cd -