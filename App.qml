import QtQuick 2.7
import QtQuick.Controls 1.4
import QtQuick.Layouts 1.3

import CustomType 1.0

ApplicationWindow {
    id: appWindow
    objectName: "appWindow"
    title: "Custom type with list property"
    visible: true
    width: 800
    height: 600

    CustomType {
      id: customType
      names: ["one", "two"]
      //names: [] // works
    }
}
