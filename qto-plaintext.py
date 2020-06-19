from PyQt5.Qt import*


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("plain TextEdit学习")
        self.resize(800,800)
        self.setup_ui()
    def setup_ui(self):
        self.btn()
        self.pte()
    def btn(self):
        btn=QPushButton("测试按钮",self)
        btn.move(20,20)
        btn.clicked.connect(self.btn_test)
    def pte(self):
        self.pte=QPlainTextEdit(self)
        self.pte.resize(500,500)
        self.pte.move(100,100)
     #调用测试的函数
    def btn_test(self):
        self.信号操作()
    def zoom(self):
        self.pte.zoomIn(10)
    def 文本操作(self):
        self.pte.setPlainText("hahahha")
        print("文本操作被调用了")
        #self.pte.insertPlainText("ooooo")
    def 信号操作(self):
        print("信号操作被调用了")
        #self.pte.textChanged.connect(lambda : print("内容发生改变 ",self.pte.toPlainText()))
        #self.pte.selectionChanged.connect(lambda :print("选中的内容发生改变" ,self.pte.textCursor().selectedText()))
        self.pte.modificationChanged.connect(lambda val:print("修改状态发生改变" ,val))
        doc=self.pte.document()
        doc.setModified(False)
       
      
        

if __name__=="__main__":
    import sys
    app=QApplication(sys.argv)
    window=Window()
    window.show()
    sys.exit(app.exec_())
