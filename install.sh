#!/bin/sh

echo "This will Install AliasMaker To Your System : (Yes => Continue, anyOther to abort)"
read RESPONSE

response1="yes"
response2="Yes"
response3="Y"
response4="y"

if [ "$RESPONSE" = "$response1" ] || [ "$RESPONSE" = "$response2" ] || [ "$RESPONSE" = "$response3" ] || [ "$RESPONSE" = "$response4" ]
then
    mkdir ~/.aliasmaker -p
    cp ./hash.hash ~/.aliasmaker/hash
    base64 -d ~/.aliasmaker/hash > ~/.aliasmaker/code.py
    echo "what do you prefer ?
1. python
2. python3 (default)"
    read PYTHON_VERSION

    if [ "$PYTHON_VERSION" -eq "1" ]
    then
      echo "
#!/bin/sh
python ~/.aliasmaker/code.py" > ~/.aliasmaker/execute
    else
      echo "
#!/bin/sh
python3 ~/.aliasmaker/code.py" > ~/.aliasmaker/execute
    fi
    chmod a+x ~/.aliasmaker/execute

    sudo rm /usr/bin/createalias || echo "checking for previous links.."
    echo "creating Link..".
    sudo ln -s ~/.aliasmaker/execute /usr/bin/createalias
    echo "process complete.."

else
    echo "aborting..."
fi