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
    echo "
#!/bin/sh
pytho3n ~/.aliasmaker/code.py" > ~/.aliasmaker/execute
    chmod a+x ~/.aliasmaker/execute

    sudo rm /usr/bin/createalias || echo "checking for previous links.."
    echo "creating Link..".
    sudo ln -s ~/.aliasmaker/execute /usr/bin/createalias
    echo "process complete.."

else
    echo "aborting..."
fi