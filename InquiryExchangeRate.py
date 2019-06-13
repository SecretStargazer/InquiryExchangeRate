import sys
import InquiryExchangeRateData
from PyQt5.QtWidgets import QApplication,QMainWindow
from InquiryExchangeRate_form import Ui_MainWindow  #导入生成的窗口
 
class MyMainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):    
        super(MyMainWindow, self).__init__(parent)
        self.setupUi(self)
        currencyList=InquiryExchangeRateData.getCurrency()
        self.currencyName1.addItems(currencyList)
        self.currencyName2.addItems(currencyList)
        self.exchangeButton.clicked.connect(self.exchange)       

    def exchange(self):
        currencyAmount1=self.currencyAmount1.text()
        currencyName1=self.currencyName1.currentText()
        currencyName2=self.currencyName2.currentText()
        if currencyName1==currencyName2:
            self.resultTextLabel.setText('错误：选择的货币种类相同')
        else:
            resuleData=InquiryExchangeRateData.getData(currencyAmount1,currencyName1,currencyName2)
            self.resultTextLabel.setText(resuleData['content1Mini'])
            self.supportTextLabel.setText(resuleData['support'])
            
if __name__=="__main__":  
    app = QApplication(sys.argv)  
    myWin = MyMainWindow()  
    myWin.show()  
    sys.exit(app.exec_())