#!/bin/sh

fileName="AliasMaker.py"
base64 "$fileName" > hash.hash
git commit -a

echo "your branch is: (default master)"
read BRANCHNAME
if [ "$BRANCHNAME" = "" ]
then
  BRANCHNAME="master"
fi

echo "Updating $BRANCHNAME"
git push origin $BRANCHNAME