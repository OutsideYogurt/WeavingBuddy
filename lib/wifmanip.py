import lib.filemanip as fm

class wifmanip():

    def __init__(self, filepath):
        self.mywiffile = fm.filemanip(filepath)
        self.wif = self._fillcategory("[WIF]")
        self.contents = self._fillcategory("[CONTENTS]")
        self.weaving = self._fillcategory("[WEAVING]")
        self.warp = self._fillcategory("[WARP]")
        self.weft = self._fillcategory("[WEFT]")
        self.colorpalette = self._fillcategory("[COLOR PALETTE]")
        self.colortable = self._fillcategory("[COLOR TABLE]")
        self.threading = self._fillcategory("[THREADING]")
        self.treadling = self._fillcategory("[TREADLING]")
        self.tieup = self._fillcategory("[TIEUP]")
        self.privatepixeloom = self._fillcategory("[PRIVATE PIXELOOM]")


    def _fillcategory(self, categoryname):
        incategory = False
        tempdict = {}
        for line in self.mywiffile.returnlines():
            if incategory == True:
                if line[0] == "[":
                    return tempdict
                else:
                    tempdict[line[:line.find("=")]] = line[line.find("=")+1:-1]
            if line[:-1] == categoryname:
                incategory = True
        return tempdict

    def printcategory(self, categoryname):
        if categoryname.lower() == "wif":
            self.printdict(self.wif)
        elif categoryname.lower() == "contents":
            self.printdict(self.contents)
        elif categoryname.lower() == "weaving":
            self.printdict(self.weaving)
        elif categoryname.lower() == "warp":
            self.printdict(self.warp)
        elif categoryname.lower() == "weft":
            self.printdict(self.weft)
        elif categoryname.lower() == "color palette":
            self.printdict(self.colorpalette)
        elif categoryname.lower() == "color table":
            self.printdict(self.colortable)
        elif categoryname.lower() == "threading":
            self.printdict(self.threading)
        elif categoryname.lower() == "treadling":
            self.printdict(self.treadling)
        elif categoryname.lower() == "tieup":
            self.printdict(self.tieup)
        elif categoryname.lower() == "private pixeloom":
            self.printdict(self.privatepixeloom)
        else:
            return False


    def printdict(self, dicttoprint):
        for key in dicttoprint:
            print(key + " = " + dicttoprint[key])

