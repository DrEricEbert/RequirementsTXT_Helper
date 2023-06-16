# -*- coding: utf-8 -*-
"""
Created on Fri Jun 16 08:29:59 2023

@author: Eric
"""

import pip
import sys
import re
import tkinter as tk
from tkinter import filedialog

from contextlib import redirect_stdout
import io
from operator import itemgetter
from collections import OrderedDict


root = tk.Tk()
root.withdraw()
root.call('wm', 'attributes', '.', '-topmost', True)
files = filedialog.askopenfilename(multiple=True,filetypes=[("requirement.txt files", "*.txt")]) 
var = root.tk.splitlist(files)
filePaths = []
for f in var:
    filePaths.append(f)


def showInfo(package):
     f = io.StringIO()
     with redirect_stdout(f):
      if hasattr(pip, 'main'):
          result = pip.main(['show', package])
          result = f.getvalue()
      else:
          result = pip._internal.main(['show', package])
          result = f.getvalue()
      tokens = result.split("\n")
      kvl = []
      for t in tokens:
          keyValue = t.split(": ")
          if len(keyValue) > 1:
              d = {keyValue[0]:keyValue[1]}
              kvl.append(d)
      return kvl
resultString = ""
for file in filePaths:
    with open(file) as myfile:
      pkgs = myfile.read()
      pkgs = pkgs.splitlines()
      infos = []
      for pkg in pkgs:
              pkgWOVersion=pkg.split('==')[0]
              info = showInfo(pkgWOVersion)
              infos.append({pkgWOVersion:info})
              if len(info) > 2:
                     cleanString = re.sub('\W+\s','', info[2]['Summary'] )+"\t"+info[3]['Home-page'] 
                     print(pkg +" -> "+cleanString)
                     resultString = resultString+(pkgWOVersion+"\t\t #"+cleanString+"\n")
              else:
                  resultString = resultString+(pkg.split('==')[0]+"\n")
      myfile.close()
      
toFile= "\n".join(list(OrderedDict.fromkeys(resultString.split("\n"))))  
with open("e:/ShareE/requirements.txt", "a", encoding='utf-8') as myfileout:
     myfileout.write(toFile)
     myfileout.close()
