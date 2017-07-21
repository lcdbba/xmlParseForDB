from xml.etree.ElementTree import parse
import os
'''
path = "main.list"
xml_home = ''
xmlPath = '../../xml/dbQuery.xml'
#xmlPath = os.path.join(xml_home,'')
tree = parse(xmlPath)
note = tree.getroot()
for row in path.split('.'):
    note = note.find(row)
print  note.text
'''
class xmlParser():
    def __init__(self, xmlName='dbQuery.xml'):
        #self.xml_path = os.path.join(xml_home, xml_name)
        basePath = "../../xml/"
        self.xmlPath = os.path.join(basePath, xmlName)
        self.tree = parse(self.xmlPath)
        self.tree = self.tree.getroot()
    #query path format : "main.list"
    #xml architect : <master> -> main -> list
    def getText(self, qry_path):
        split_qry = qry_path.split('.')
        rst = self.tree
        for row in split_qry:
            rst = rst.find(row)
        return rst.text
