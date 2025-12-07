import sys
from PyQt6.QtWidgets import *

class App(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("SEO Анализ")
        self.body()
    
    def body(self):
        self.setGeometry(100, 100, 500, 700)

        first_widget = QWidget()
        self.setCentralWidget(first_widget)
        
        main_layout = QVBoxLayout()
        first_widget.setLayout(main_layout)

        self.text_zone = QTextEdit()
        self.text_zone.setPlaceholderText("Текст вводится сюда.")
        main_layout.addWidget(self.text_zone)
        
        self.button = QPushButton()
        self.button.setText("АНАЛИЗ")
        self.button.clicked.connect(self.one_click)
        main_layout.addWidget(self.button)

        self.box = QCheckBox()
        self.box.setText("Калькулятор вместо SEO анализа")
        main_layout.addWidget(self.box)

        self.out_zone = QTextEdit()
        self.out_zone.setPlaceholderText("Результат")
        self.out_zone.setReadOnly(True)
        main_layout.addWidget(self.out_zone)

    def one_click(self):
        
        # Если в боксе стоит галочка, тогда в поле результата будет выводиться значение
        if self.box.isChecked():
            text = self.text_zone.toPlainText().strip()
            try:
                res = eval(text)
                self.out_zone.setPlainText(str(eval(text)))
            except SyntaxError:
                QMessageBox.warning(self, "Ошибка", "Неверный формат ввода для калькулятора!")

        # Если в боксе не стоит галочка, тогда в поле будет SEO анализ
        else:
            text = self.text_zone.toPlainText().strip()
            if text == "":
                QMessageBox.warning(self, "Пустой ввод", "Введите что-нибудь!")
                return 0   
            words = text.split()
            chars = len(text)
            words_count = len(words)
            uniqe_words = set(word.lower().strip(',.!?(){}[]"\'') for word in words)
            uniqe_words_count = len(uniqe_words)
            no_spaces = len(text.replace(" ", ""))
            sentences = text.count(".") + text.count("!") + text.count("?")
            result = f"""Колличество символов: {chars}
Колличество символов без пробелов: {no_spaces}
Колличество слов: {words_count}
Колличество уникальных слов: {uniqe_words_count}
Колличество предложений: {sentences}
            """
            self.out_zone.setPlainText(result)


if __name__ == '__main__':
    app = QApplication(sys.argv)

    app.setStyle("Fusion")

    window = App()
    window.show()

    sys.exit(app.exec())
