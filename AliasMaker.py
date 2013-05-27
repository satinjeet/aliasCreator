import os
import json
from pprint import pprint
import shutil

class AppError(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)

class Application:
    home = os.getenv("HOME")
    appDir = os.getenv("HOME") + "/.aliasmaker"
    aliasFile = "aliases.sh"
    aliasJSON = "alias.json"
    backup = "alias.json.back"
    rawData = """{
    "shell": "zshrc",
    "aliases": {
        "ls": "ls",
        "clear": "clear"
    }
}
"""

    def __boot__(self):
        self.__isAppDirThere().__findAndCreateJSON().__backUp()

        #fileOps
        filePath = self.appDir + "/" + self.aliasJSON
        
        fileOps = FileOperations()
        fileOps.EditFile(filePath)
        exports = fileOps.parseJson(filePath)
        self.writeShFile(exports[1]).linkSh(exports[0])
 
    def __isAppDirThere(self):
        if os.path.exists(self.appDir):
            print("Found Application..")
        else:
            print("Creating Dir....")
            os.makedir(self.appDir)
        return self           

    def __findAndCreateJSON(self):
        jsonFile = self.appDir + "/" + self.aliasJSON

        if os.path.exists(jsonFile):
            print("Source File Found...")
        else:
            print("creating meta source file...")
            obj = open(jsonFile, "w")
            obj.write(self.rawData)
            obj.close()
        return self

    def __backUp(self):
        srcfile = self.appDir + "/" + self.aliasJSON
        backupfile = self.appDir + "/" + self.backup
        shutil.copy(srcfile, backupfile)

    def writeShFile(self, exports):
        seperator = "\n"
        shData = seperator.join(exports)
        sh = self.appDir + "/" + self.aliasFile
        print("creating sh file...")
        sh = open(sh, "w")
        sh.write(shData)
        sh.close()
        return self

    def linkSh(self, shellFile):
        
        commandLink = "\nsource \"" + self.appDir + "/" + self.aliasFile + "\""
        if not commandLink in open(self.home + "/." + shellFile, "r").read():
            print("linking with Shell File")
            sh = self.home + "/." + shellFile
            sh = open(sh, "a+")
            sh.write(commandLink)
            sh.close()
        else:
            print("link Exists")

class FileOperations:
    editors = ["gedit", "vi", "emacs"]

    def EditFile(self, filePath):
        option = raw_input("select your editor (1. gedit, 2. vim, 3.emacs 4. other ... enter to skip) ? ")
        editor = ""
        if option is "":
            editor = "cat"
        elif int(option) < 4:
            editor = self.editors[int(option)-1]
        else:
            editor = str(raw_input("enter your editor: "))

        command = editor + " " +filePath
        return os.system(command)

    def parseJson(self, filePath):
        jsonFile=open(filePath)
        data = json.load(jsonFile)
        jsonFile.close()

        exports = []
        aliases = data['aliases']
        shell = data['shell']
        keys = aliases.keys()
        for key in keys:
            exports.append("alias " + key + "=" + "\"" + aliases[key] +"\"")

        return [shell, exports]

app = Application()
app.__boot__()
    
