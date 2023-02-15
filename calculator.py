from PyQt5.QtWidgets import QWidget,QApplication,QLabel,QLineEdit,QPushButton

app=QApplication([])
oyna=QWidget()
oyna.setFixedSize(450,500)
oyna.setStyleSheet("background:lightgray")

edit=QLineEdit(oyna)
edit.setFixedSize(440,80)
edit.setStyleSheet("margin-left:8px;margin-top:10px;border:none;font-size:45px;background:white")

l=QLabel(oyna)
l.setGeometry(8,100,432,80)
l.setStyleSheet("background:silver;font-size:45px")

def info():
    l.setText(str(eval(edit.text())))
    edit.clear()

btn=QPushButton("=",oyna)
btn.setGeometry(150,250,150,150)
btn.clicked.connect(info)
btn.setStyleSheet("background:gray;border:none;font-size:50px")

oyna.show()
app.exec_()