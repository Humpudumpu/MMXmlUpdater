__author__ = 'Nikhil'

import xml.etree.ElementTree as ET
tree = ET.parse("AuchanFranceCommon.xml")
root = tree.getroot()
for styleElement in root.iter("Style"):
    for fontElement in styleElement.iter("Font"):
        if fontElement.text == "Arial":
            print(styleElement.attrib, end="")
            for sizeElement in styleElement.iter("Size"):
                print(" Size =  "+sizeElement.text)
