__author__ = 'Nikhil'

import xml.etree.ElementTree as ET
import shutil
import os
import contextlib
import mmap

multimediaFilePath = "AuchanFranceCommon.xml"
multimediaFilePath_Edited = "AuchanFranceCommon_edited.xml"
mmDoc = ET.parse(multimediaFilePath)
root = mmDoc.getroot()
if os.path.exists(multimediaFilePath_Edited):
    os.remove(multimediaFilePath_Edited)
shutil.copyfile(multimediaFilePath, multimediaFilePath_Edited)
affectedFonts = []
for styleNode in root.iter("Style"):
    arialNarrow = False
    styleNodeName = styleNode.attrib["Name"]
    for subNodes in styleNode.getchildren():
        if subNodes.tag == "Font" and subNodes.text == "Arial Narrow":
            arialNarrow = True
        if subNodes.tag == "Size" and arialNarrow:
            print(" Name: ", styleNodeName, end=" ::  ")
            print(" Current Size: ", subNodes.text, end=" <> ")
            subNodes.text = int(subNodes.text) - 2
            print(" New Size: ", subNodes.text)
            affectedFonts.append(styleNodeName)

for font in affectedFonts:
    print(font)

for childNodes in root.iter():
    if hasattr(childNodes, "Style"):
        for subSizeChildNodes in childNodes:
            if subSizeChildNodes.tag == "Size":
                print("Changed font size for element :" + childNodes.get("Name") + subSizeChildNodes.text + " to ", end="")
                subSizeChildNodes.text = int(subSizeChildNodes.text) - 2
                print(subSizeChildNodes.text)