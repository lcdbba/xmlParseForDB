from ConfigParser import ConfigParser
import sys
import os
#import pypath #--> sys.path.append("${module path}$")
base_home = '/Users/ybam/Dropbox/modules'
conf_home = os.path.join(base_home, "conf")

class confParse():
    def __init__(self, filename=''):
        if filename != '':
            self.conf = ConfigParser()
            self.filepath = os.path.join(conf_home, filename)
            self.conf.read(self.filepath)
            self.sections = self.conf.sections()

    def getSections(self):
        return self.conf._sections

    def getSection(self, section):
        return self.conf._sections[section]

    def getValue(self, section, option):
        return self.conf.get(section,option)

    def setSection(self, sectionName):
        self.conf.add_section(sectionName)

    def setOptions(self, sectionName, options):
        f = open(self.filepath, 'w')
        for key in options.keys():
            self.conf.set(sectionName, key, options[key])
            self.conf.write(f)
        f.close()
