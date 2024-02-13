import sys
from PySide6 import QtWidgets
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget
from PySide6.QtSql import QSqlTableModel
from design import Ui_MainWindow
from design2 import Ui_Dialog
from connection import Data

class TaskManager(QMainWindow):
    def __init__(self):
        super(TaskManager, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.conn = Data()
        self.view_data()
        self.ui.btn_add.clicked.connect(self.open_new_task_window)
        self.ui.btn_delete.clicked.connect(self.delete_task)
        self.add_count = 0
        self.dec_count = 0

    def view_data(self):
        self.model = QSqlTableModel(self)
        self.model.setTable('tasks')
        self.model.select()
        self.ui.tableView.setModel(self.model)
        
    
    def open_new_task_window(self):
        self.new_window = QtWidgets.QDialog()
        self.ui_window = Ui_Dialog()
        self.ui_window.setupUi(self.new_window)
        self.new_window.show()
        sender = self.sender()
        if sender.text() == "Добавить задачу":
            self.ui_window.btn_savetask.clicked.connect(self.add_new_task)
        
           
    def add_new_task(self):
        date = self.ui_window.data.text()
        name = self.ui_window.taskdesc.text()
        self.conn.add_new_task_query(date, name)
        self.view_data()
        self.add_count += 1
        self.ui.activecount.setText(str(self.add_count))
        self.new_window.close()
        
    def delete_task(self):
        index = self.ui.tableView.selectedIndexes()[0]
        id = str(self.ui.tableView.model().data(index))
        self.conn.delete_task_query(id)
        self.view_data()
        self.dec_count += 1
        self.ui.donecount.setText(str(self.dec_count))
        if self.add_count > 0:
            self.add_count -= 1
            self.ui.activecount.setText(str(self.add_count)) 
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = TaskManager()
    window.show()
    sys.exit(app.exec())   
            