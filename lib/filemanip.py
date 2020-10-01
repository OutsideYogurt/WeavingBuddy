'''
simple class that is use to quickly deal with files.
should be use for common simple file manipulation like remove line, adding line, creating a new file.

was originaly created to edit move file and deal with packages.
'''

class filemanip():
    def __init__(self, filepath=None):
        self.filepath = filepath
        self.thefile = None
        self.originalcontent = None

    def _openfile(self, mode="r"):
        self.thefile = open(self.filepath, mode)
        #print("the file is open")

    def _closefile(self):
        self.thefile.close()
        #print("the file is closed")

    def _readoriginalfile(self):
        self._openfile("r")
        self.originalcontent = self.thefile.readlines()
        self._closefile()

    def _writefile(self, content):
        self.thefile.write(content)

    def _stringtolist(self, amialist):
        if type(amialist) is str:
            return [amialist]
        else:
            return amialist

    def createfile(self, name, path, extension, content=None):
        self.filepath = path + name + extension
        self._openfile("w")
        if content is not None:
            self._writefile(content)
        self._closefile()

    def removelinewiththisstring(self, listofstringtolookfor):
        try:
            listofstringtolookfor = self._stringtolist(listofstringtolookfor)
            self._readoriginalfile()
            self._openfile("w")
            for lines in self.originalcontent:
                stringfound = False
                for x in listofstringtolookfor:
                    if lines.find(x) != -1:
                        stringfound = True
                if stringfound is False:
                    self._writefile(lines)
        finally:
            self._closefile()

    def replacelinewiththisstringbythisline(self, listofstringtolookfor, linetoreplacwith):
        try:
            listofstringtolookfor = self._stringtolist(listofstringtolookfor)
            self._readoriginalfile()
            self._openfile("w")
            for lines in self.originalcontent:
                stringfound = False
                for x in listofstringtolookfor:
                    if lines.find(x) != -1:
                        stringfound = True
                        self._writefile(linetoreplacwith)
                if stringfound is False:
                    self._writefile(lines)
        finally:
            self._closefile()

    def replacestringsbythisstring(self, listofstringtolookfor, toreplacewith):
        try:
            listofstringtolookfor = self._stringtolist(listofstringtolookfor)
            self._readoriginalfile()
            self._openfile("w")
            for lines in self.originalcontent:
                for x in listofstringtolookfor:
                    if lines.find(x) != -1:
                        lines = lines.replace(x, toreplacewith)
                self._writefile(lines)
        finally:
            self._closefile()

    def insertlinebefore(self, whatimlookingfor, linetoinsert):
        try:
            self._readoriginalfile()
            self._openfile("w")
            for lines in self.originalcontent:
                # all this formated thing is to keep the indentation of the line.
                formatedlinetoinsert = linetoinsert
                if lines.find(whatimlookingfor) != -1:
                    for x in range(lines.find(whatimlookingfor)):
                        formatedlinetoinsert = "\t" + formatedlinetoinsert
                    self._writefile(formatedlinetoinsert)
                self._writefile(lines)
        finally:
            self._closefile()

    def searchstring(self, whatimlookingfor):
        # probably super slow because if this is call by searchstrings I will read the file for each different string
        # I'm looking for. Need to rethink that.
        self._readoriginalfile()
        stringofmylist = ''.join(self.originalcontent)
        if stringofmylist.find(whatimlookingfor) != -1:
            return True
        else:
            return False

    def searchstrings(self, whatimlookingfor):
        for item in whatimlookingfor:
            if self.searchstring(item) is True:
                return True
        return False

    def printfile(self):
        self._openfile("r")
        for line in self.thefile.readlines():
            print(line)
        self._closefile()

    def returnlines(self):
        self._openfile("r")
        for line in self.thefile.readlines():
            yield line
        self._closefile()

