from PyQt5.QtWidgets import QMainWindow, QApplication , QFileDialog
from PyQt5.QtPrintSupport import QPrinter, QPrintDialog
from PyQt5.uic import loadUi
import sys

class texteditor(QMainWindow):
    def __init__(self):
        super(texteditor, self).__init__()
        loadUi("main.ui", self)
        
        self.textEdit.textChanged.connect(self.countWords)
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
        
        self.setWindowTitle("Untitled")
        self.current_path = None
        self.statusBar().showMessage("Ready")
    
    def newFile(self):
        self.textEdit.clear()
        self.setWindowTitle("Untitled")
        self.current_path = None

        
    def openFile(self):
        fname = QFileDialog.getOpenFileName(self, 'Open file', 'home\Documents', 'Text files (*.txt)')
        self.setWindowTitle(fname[0])
        with open(fname[0], 'r') as f:
            filetext = f.read()
            self.textEdit.setText(filetext)
        self.current_path = fname[0]
        
    def saveFile(self):
        if self.current_path is not None:
            # save the changes without opening dialog
            filetext = self.textEdit.toPlainText()
            with open(self.current_path, 'w') as f:
                f.write(filetext)
        else:
            self.saveFileAs()
      
    def saveFileAs(self):
    	default_name = "Untitled"
    	pathname = QFileDialog.getSaveFileName(self, 'Save file',default_name , 'Text files(*.txt)')
        filetext = self.textEdit.toPlainText()
        with open(pathname[0], 'w') as f:
            f.write(filetext)
        self.current_path = pathname[0]
        self.setWindowTitle(pathname[0])
        
    def countWords(self):
    	text = self.textEdit.toPlainText()
    	word_count = len(text.split())
    	self.statusBar().showMessage("Word count: "+str(word_count))
    	  
    def printFile(self):
    	printer = QPrinter(QPrinter.HighResolution)
    	dialog = QPrintDialog(printer, self)
    	
    	if dialog.exec_() == QPrintDialog.Accepted:
    	    self.textEdit.print_(printer)
    
    def closeFile(self):
        self.close()
        
    def undo(self):
    	self.textEdit.undo()
    
    def redo(self):
    	self.textEdit.redo()
        
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
    	
if __name__ == "__main__":
    app = QApplication(sys.argv)
    ui = texteditor()
    ui.show()
    app.exec_()
