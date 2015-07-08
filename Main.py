__author__ = 'Nikhil'

import xml.etree.ElementTree as ET
import shutil
import os
import contextlib
import mmap

# Function to find the style node with font = Arial Narrow
def FindUpdateRequiredStyleNodes (root):
    affectedFonts = []
    for styleNodes in root.findall(".//MultiLang/Style[Font='Arial Narrow']"):
        print(" Affected font node : "+ styleNodes.attrib["Name"], end=" <> ")
        affectedFonts.append(styleNodes.attrib["Name"])
        for fontNodes in styleNodes.findall(".//Font"):
            print("Old font : " + fontNodes.text, end=" <> ")
            fontNodes.text = "Arial"
            print("New font : " + fontNodes.text, end=" <> ")
        for sizeNodes in styleNodes.findall(".//Size"):
            print("Old font size: ", sizeNodes.text, end=" <> ")
            sizeNodes.text = int(sizeNodes.text) - 2
            print("New font size: ", sizeNodes.text)
    return affectedFonts

multimediaFilePath = "AuchanFranceCommon.xml"
multimediaFilePath_Edited = "AuchanFranceCommon_edited.xml"
mmDoc = ET.parse(multimediaFilePath)
root = mmDoc.getroot()
if os.path.exists(multimediaFilePath_Edited):
    os.remove(multimediaFilePath_Edited)

affectedFonts = FindUpdateRequiredStyleNodes(root)

