import tkinter as tk
import re
from tkinter import filedialog
root = tk.Tk()
root.withdraw()
#
Folderpath = filedialog.askdirectory()
# Filepath = filedialog.askopenfilenames()
name = filedialog.asksaveasfilename()
print('name+++',name)
print('folder',Folderpath)
# m=re.findall(r'(.+?)\.',name)
m = re.findall(r'\.[^.\\/:*?"<>|\r\n]+$', name)

if(m):
    print('++++++++++',m[0])
else:
    print('++++++++++','empty',name+'.pdf')
# paths = list(Filepath)
# print('file',type(Filepath),Filepath)
