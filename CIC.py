__author__ = "Foleevora"
__version__ = "1.0.0"
__email__ = "foleevora@gmail.com"

import sys
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFilter
from PyQt5 import QtWidgets
from PyQt5 import QtGui
from PyQt5 import uic
from PyQt5 import QtCore
from PyQt5.QtCore import pyqtSlot

class Form(QtWidgets.QDialog):
    def __init__(self, parent=None):
        QtWidgets.QDialog.__init__(self, parent)
        self.ui = uic.loadUi("CIC.ui", self)
        self.ui.show()

    @pyqtSlot()
    def slot_file(self):
        fname, _ = QtWidgets.QFileDialog.getOpenFileName(self, 'Open file', '/Users',"Image files (*.jpg *.gif *.jpeg *.png)")
        self.ui.edit_file.setText(str(fname))

    @pyqtSlot()
    def slot_convert(self):
        base = Image.open(self.ui.edit_file.text()).convert('RGBA').rotate(22)
        base.filter(ImageFilter.BLUR)
        img = Image.new('RGBA', base.size, (255,255,255,255))
        draw = ImageDraw.Draw(img)
        draw.line((0, img.size[1]/4) + img.size, fill="#9FF8BE", width=30)
        draw.line((0, img.size[1]-img.size[1]/4.3, img.size[0], 0), fill="#9FF8BE", width=120)
        out = Image.blend(base, img, 0.36)
        out.save('coolImage.png')



if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    w = Form()
    sys.exit(app.exec())
