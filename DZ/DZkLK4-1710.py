import sys 
from PyQt6.QtWidgets import QApplication, QWidget, QLabel
from PyQt6.QtGui import QPixmap

class MainWindow(QWidget):
    
    def __init__(self):
        super().__init__()
        self.initializeUI()
        
    def initializeUI(self):
        """Настройка приложения."""
        self.setGeometry(300, 300, 250, 250)
        self.setWindowTitle("Картинка")
        
        self.setUpMainWindow()
        self.show() # Отображение окна на экране
       
     
    def setUpMainWindow(self):
        """Создайте QLabel для отображения в главном окне."""
    
        hello_label = QLabel(self)
        hello_label.setText("Здрасьте!")
        hello_label.move(105, 15)
        image = "/Users/anton_ilchenko/Documents/DATEBASE/DZkLK4-1710/DZ/img1.jpg"
        try:
            with open(image):
                world_label = QLabel(self)
                pixmap = QPixmap(image)
                scaled_pixmap = pixmap.scaled(200, 150)
                world_label.setPixmap(scaled_pixmap)
                world_label.move(25, 40)
        except FileNotFoundError as error:
            print(f"Image not found.\nError: {error}")
        

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())