from PyPDF2 import PdfFileReader,PdfFileWriter
import tkinter as tk
from tkinter import filedialog
import re
def merge_pdfs(paths,output):
    pdf_writer = PdfFileWriter()
    for path in paths:
        pdf_reader = PdfFileReader(path)
        for page in range(pdf_reader.getNumPages()):
            pdf_writer.addPage(pdf_reader.getPage(page))
    with open(output,'wb') as out:
        pdf_writer.write(out)

if __name__ =='__main__':
    root = tk.Tk()
    root.withdraw()
   
    Filepath = filedialog.askopenfilenames()
  
    paths = list(Filepath)
    # print('file',type(Filepath),Filepath)
    # Folderpath = filedialog.askdirectory()
    # print('folder',Folderpath)
    name = filedialog.asksaveasfilename()
    m = re.findall(r'\.[^.\\/:*?"<>|\r\n]+$', name)
    if(m):
        if(m[0] == '.pdf' or m[0] == '.PDF' ):
            merge_pdfs(paths,output = name)
        else:
            merge_pdfs(paths,output = name+'.pdf')
    else:
        merge_pdfs(paths,output = name+'.pdf')
    # paths = ['C:/Users/dilmuratalim/Desktop/files/编写的软件-方法/关于Python/python操作PDF/文件/f-麻绳.pdf','C:/Users/dilmuratalim/Desktop/files/编写的软件-方法/关于Python/python操作PDF/文件/f-小刀.pdf']
    # merge_pdfs(paths,output = 'C:/Users/dilmuratalim/Desktop/files/编写的软件-方法/关于Python/python操作PDF/文件/合并.pdf')