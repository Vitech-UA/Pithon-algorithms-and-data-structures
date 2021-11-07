import QtQuick 2.5
import QtQuick.Controls 1.4
import QtQuick.Layouts 1.2

ApplicationWindow{
    visible: true
    width:640
    height:240
    title: qsTr("PyQt")
    color: "whitesmoke"
    GridLayout{
        anchors.top: parent.top
            anchors.left: parent.left
            anchors.right: parent.right
            anchors.margins: 9

            columns: 4
            rows: 4
            rowSpacing: 10
            columnSpacing: 10

            Text{
            text: qsTr("First number")
            }
            TextField{
            id: firstNumber
            }

            Text{
            text: qsTr("Second number")
            }
            TextField{
            id: secondNumber
            }

            Button{
            height:40
            Layout.fillWidth: true
            text: qsTr("Додати числа")
            Layout.columnSpan:2
            onClicked:{
              //Виклик слота калькулятора
              calculator.sum(firstNubber.text, secondNumber.text)
             }
            }
            Text {
            text: qsTr("Result")

            Text {
                id: sumResult
        }
            Button {
                height: 40
                Layout.fillWidth: true
                text: qsTr("Відняти числа")

                Layout.columnSpan: 3

                onClicked: {
                    // Виклик слота віднімання
                    calculator.sub(firstNumber.text, secondNumber.text)
                }
            }
        Text {
            text: qsTr("Result")
        }

        // Здесь увидим результат вычитания
        Text {
            id: subResult
        }
        }
    }
 Connections {
        target: calculator

        // Обработчик сигнала сложения
        onSumResult: {
            // sum было задано через arguments=['sum']
            sumResult.text = sum
        }

        // Обработчик сигнала вычитания
        onSubResult: {
            // sub было задано через arguments=['sub']
            subResult.text = sub
        }
    }
}