#!/bin/sh

fileName="AliasMaker.py"
base64 "$fileName" > hash.hash
git commit -a

echo "your branch is: "
read $BRANCHNAME
git push origin "$BRANCHNAME"