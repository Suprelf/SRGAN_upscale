import sys
import time
from methods import Interpolation
from mode import *
import argparse
from PyQt6.QtWidgets import QApplication, QMainWindow, QFileDialog
import InterfaceTemplate


class Window(QMainWindow, InterfaceTemplate.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.inputPath = ''
        self.outputPath = ''
        self.method = ''

        self.pushButton.clicked.connect(self.handlerOpenInput)
        self.pushButton_2.clicked.connect(self.handlerOpenOutput)
        self.pushButton_3.clicked.connect(self.handlerStart)
        self.pushButton_4.clicked.connect(self.handlerStop)

        self.radios = \
            [self.radioButton, self.radioButton_2, self.radioButton_3,
             self.radioButton_4, self.radioButton_5]
        for radio in self.radios:
            radio.toggled.connect(self.handlerSelection)

    def handlerOpenInput(self):
        self.lineEdit.setDisabled(False)
        dirPath = str(QFileDialog.getExistingDirectory(self, "Select input folder"))
        self.lineEdit.setText(dirPath)
        self.inputPath = dirPath
        self.lineEdit.setDisabled(True)

    def handlerOpenOutput(self):
        self.lineEdit_2.setDisabled(False)
        dirPath = str(QFileDialog.getExistingDirectory(self, "Select output folder"))
        self.lineEdit_2.setText(dirPath)
        self.outputPath = dirPath
        self.lineEdit_2.setDisabled(True)

    def handlerSelection(self):
        for items in self.radios:
            if items.isChecked():
                self.method = items.objectName()
                print(self.method)

    def handlerStop(self):
        print()

    def handlerStart(self):
        if (self.inputPath == '' or
                self.outputPath == '' or
                self.method == ''):
            self.label_3.setText('Fill all the fields!')
        else:
            start = time.time()
            self.label_3.setText('Processing...')
            print(self.outputPath, '--->', self.inputPath)

            if self.method == "l":
                print("l started")
                Interpolation(self.inputPath+'/', self.outputPath+'/', "l")

            if self.method == "b":
                print("b started")
                Interpolation(self.inputPath+'/', self.outputPath+'/', "b")

            if self.method == "s" or "ls" or "bs":
                print("srgan (+ methods) started")

                if self.method == "ls":
                    print("l in ls started")
                    Interpolation(
                        self.inputPath + '/',
                        'C:/Users/Olek/Desktop/SRGAN2/LR/interpolated/',
                        "l")
                    self.inputPath = 'C:/Users/Olek/Desktop/SRGAN2/LR/interpolated'

                if self.method == "bs":
                    print("b in bs started")
                    Interpolation(
                        self.inputPath + '/',
                        'C:/Users/Olek/Desktop/SRGAN2/LR/interpolated/',
                        "b")
                    self.inputPath = 'C:/Users/Olek/Desktop/SRGAN2/LR/interpolated'

                parser = argparse.ArgumentParser()

                def str2bool(v):
                    return v.lower() in ('true')

                parser.add_argument("--LR_path", type=str,
                                    default=self.inputPath)
                parser.add_argument("--GT_path", type=str,
                                    default=self.outputPath)
                parser.add_argument("--res_num", type=int, default=16)
                parser.add_argument("--num_workers", type=int, default=0)
                parser.add_argument("--batch_size", type=int, default=16)  # 16
                parser.add_argument("--L2_coeff", type=float, default=1.0)
                parser.add_argument("--adv_coeff", type=float, default=1e-3)
                parser.add_argument("--tv_loss_coeff", type=float, default=0.0)
                parser.add_argument("--pre_train_epoch", type=int, default=8000)  # 8000
                parser.add_argument("--fine_train_epoch", type=int, default=4000)  # 4000
                parser.add_argument("--scale", type=int, default=4)
                parser.add_argument("--patch_size", type=int, default=24)
                parser.add_argument("--feat_layer", type=str, default='relu5_4')
                parser.add_argument("--vgg_rescale_coeff", type=float, default=0.006)
                parser.add_argument("--fine_tuning", type=str2bool, default=False)
                parser.add_argument("--in_memory", type=str2bool, default=True)
                parser.add_argument("--generator_path", type=str,  ##here be model change
                                    default='C:/Users/Olek/Desktop/SRGAN2/models/SRGAN.pt')
                parser.add_argument("--mode", type=str, default='test_only')

                args = parser.parse_args()
                test_only(args)

                elapsed = time.time() - start
                self.label_4.setText("Completed in: " + str(elapsed) + "s")
                self.label_3.setText("Finished!")







if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    app.exec()
