from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog,Qmessagebox
from PyQt5.uic import loadUi
from PyQt5.QtPrintSupport import QPrinter,QPrintDialog,QPrintPreviewDialog
from PyQt5.QtCore import QFileInfo
import sys


class texteditor(QMainWindow):
    def __init__(self):
        super(texteditor, self).__init__()
        loadUi("main.ui", self)
        
        self.actionNew.triggered.connect(self.newFile)
        self.actionOpen.triggered.connect(self.openFile)
        self.actionSave.triggered.connect(self.saveFile)
        self.actionSave_as.triggered.connect(self.saveFileAs)
        self.actionPrint.triggered.connect(self.printFile)
        self.actionClose.triggered.connect(self.closeFile)
        self.actionUndo.triggered.connect(self.undo)
        self.actionRedo.triggered.connect(self.redo)
        self.actionCut.triggered.connect(self.cut)
        self.actionCopy.triggered.connect(self.copy)
        self.actionPaste.triggered.connect(self.paste)
        self.actionLayouts.triggered.connect(self.layouts)
        self.actionMode.triggered.connect(self.modes)
    	self.actionExport_PDF.triggered.connect(self.exportPdf)
    	self.actionPrint_Preview.triggered.connect(self.printPreview)
    	
    def newFile(self):
        self.textEdit.clear()
        self.setWindowTitle("Untitled")
        self.current_path = None

        
    def openFile(self):
        print("clicked on open file")
        
    def saveFile(self):
        if self.current_path is not None:
            # save the changes without opening dialog
           filetext = self.textEdit.toPlainText()
           with open(self.current_path, 'w') as f:
               f.write(filetext)
                
    def saveFileAs(self):
    	print("clicked on save file as")
  
    def printFile(self):
    	print("clicked on print file")
    
    def closeFile(self):
    	print("clicked on close file")
        
    def undo(self):
    	print("clicked on undo")
    
    def redo(self):
    	print("clicked on redo")
        
    def cut(self):
    	self.textEdit.cut()
    
    def copy(self):
    	self.textEdit.copy()
        
    def paste(self):
    	self.textEdit.paste()
        
    def layouts(self):
    	print("clicked on layouts")
        
    def modes(self):
    	print("clicked on modes")
    
    def exportPdf(self):
    		fn, _  =QfileDialog.getSaveFileName(self,"Export PDF",None,"PDF files (.pdf) ;; All Files")
        if fn !="":
        		if QFileInfo(fn).suffix()=="" :fn += '.pdf'
            printer=QPrinter(Qprinter.HighResolution)
            printer.setOutputFormat(QPrinter.PdfFormat)
            printer.setOutputFileName(fn)
            self.textEdit.document().print_(printer)
    
    def printPreview(self):
    		printer=QPrinter(QPrinter.HighResolution)
        previewDialog=QPrintPreviewDialog(printer,self)
        previewDialog.paintRequested.connect(self.printPreview)
        previewDialog.exec()
    
    def printPreview(self,printer):
    		self.textEdit.print_(printer)
if __name__ == "__main__":
    app = QApplication(sys.argv)
    ui = texteditor()
    ui.show()
    app.exec_()
