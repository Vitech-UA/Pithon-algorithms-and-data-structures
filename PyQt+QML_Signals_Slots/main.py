from PyQt5.QtGui import QGuiApplication
from PyQt5.QtQml import QQmlApplicationEngine
from PyQt5.QtCore import QObject, pyqtSignal, pyqtSlot


class Calculator(QObject):
    def __init__(self):
        QObject.__init__(self)

    '''Сигнали, що передають суму і різницю. 
     Обов'язково даємо назву аргументу через arguments=['sum'], щоб забрати його з QML '''
    sumResult = pyqtSignal(int, arguments=['sum'])
    subResult = pyqtSignal(int, arguments=['sub'])

    '''Слот для сумування двох чисел '''

    @pyqtSlot(int, int)
    def sum(self, arg1, arg2):
        self.sumResult.emit(arg1 + arg2)

    @pyqtSlot(int, int)
    def sub(self, arg1, arg2):
        self.subResult.emit(arg1 - arg2)


if __name__ == "__main__":
    import sys

    # створюю екземпляр додатку
    app = QGuiApplication(sys.argv)
    # запускаю QML движок
    engine = QQmlApplicationEngine()
    # створюю об'єкт калькулятора
    calculator = Calculator()
    # реєструю його в контексті QML
    engine.rootContext().setContextProperty("calculator", calculator)
    # ззавантажуємо файл qml у движок
    engine.load("main.qml")

    engine.quit.connect(app.quit)
    sys.exit(app.exec_())
