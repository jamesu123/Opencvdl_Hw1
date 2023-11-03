# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui55.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.
import cv2
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PIL import Image
from PIL.ImageQt import ImageQt

from scipy import signal

from PyQt5 import QtCore, QtGui, QtWidgets

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 506)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(130, 70, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(100, 110, 169, 241))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton_2 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout.addWidget(self.pushButton_2)
        self.pushButton_3 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_3.setObjectName("pushButton_3")
        self.verticalLayout.addWidget(self.pushButton_3)
        self.pushButton_4 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_4.setObjectName("pushButton_4")
        self.verticalLayout.addWidget(self.pushButton_4)
        self.pushButton_5 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_5.setObjectName("pushButton_5")
        self.verticalLayout.addWidget(self.pushButton_5)
        self.pushButton_6 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_6.setObjectName("pushButton_6")
        self.verticalLayout.addWidget(self.pushButton_6)
        self.graphicsView = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(320, 100, 331, 341))
        self.graphicsView.setObjectName("graphicsView")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(340, 60, 160, 31))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(
            self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_3 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.label_4 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout.addWidget(self.label_4)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setGeometry(
            QtCore.QRect(340, 0, 191, 51))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(
            self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.label = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 25))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate(
            "MainWindow", "2022OpenCvDl Hw1_05"))
        self.pushButton.setText(_translate("MainWindow", "Load Image"))
        self.pushButton.clicked.connect(self.onButtonClick)

        self.pushButton_2.setText(_translate("MainWindow", "1.Show Images"))
        self.pushButton_2.clicked.connect(self.onButtonClick2)

        self.pushButton_3.setText(_translate(
            "MainWindow", "2.Show Model Structure"))
        self.pushButton_3.clicked.connect(self.onButtonClick3)

        self.pushButton_4.setText(_translate(
            "MainWindow", "3.Show Data Augmentation"))
        self.pushButton_4.clicked.connect(self.onButtonClick4)

        self.pushButton_5.setText(_translate(
            "MainWindow", "4.Show Accuracy And Loss"))
        self.pushButton_5.clicked.connect(self.onButtonClick5)

        self.pushButton_6.setText(_translate("MainWindow", "5.Inference"))
        self.pushButton_6.clicked.connect(self.onButtonClick6)

        self.label_3.setText(_translate("MainWindow", "Confidence"))
        self.label_4.setText(_translate("MainWindow", "0"))
        self.label_2.setText(_translate("MainWindow", "Prediction Label:"))
        self.label.setText(_translate("MainWindow", "Image"))

    def onButtonClick(self):  # load image
        filename, filetype = QFileDialog.getOpenFileName(None,
                                                         "選取檔案",
                                                         "./")
        print(filename)
        # self.label.setText(filename)
        self.img = filename

        frame = QImage(filename)
        pix = QPixmap.fromImage(frame)
        pix = pix.scaled(300, 300)
        item = QGraphicsPixmapItem(pix)
        scene = QGraphicsScene()
        scene.addItem(item)
        self.graphicsView.setScene(scene)

    def onButtonClick2(self):  # 5-1 Show Images
        print('Now Loading...')
        import matplotlib.pyplot as plt
        import numpy
        import tensorflow as tf
        from keras.datasets import cifar10
        import numpy as np
        import random

        labels = {0: "airplane", 1: "automobile", 2: "bird", 3: "cat", 4: "deer",
                  5: "dog", 6: "frog", 7: "horse", 8: "ship", 9: "truck"}

        # load dataset
        (trainX, trainy), (testX, testy) = tf.keras.datasets.cifar10.load_data()
        # summarize loaded dataset
        #print('Train: X=%s, y=%s' % (trainX.shape, trainy.shape))
        #print('Test: X=%s, y=%s' % (testX.shape, testy.shape))

        fig, axes = plt.subplots(ncols=3, nrows=3, figsize=(17, 8))
        index = random.randint(0, 1000)
        for i in range(3):
            for j in range(3):
                axes[i, j].set_title(labels[trainy[index][0]])
                axes[i, j].imshow(trainX[index])
                axes[i, j].get_xaxis().set_visible(False)
                axes[i, j].get_yaxis().set_visible(False)
                index += 1
        plt.show()

    def onButtonClick3(self):  # 5-2 Show Model Structure
        import os
        import cv2
        import numpy as np
        from keras.applications.vgg19 import VGG19
        from keras.applications.vgg16 import VGG16
        import tensorflow
        from PIL import Image
        from tensorflow import keras
        from keras.applications.vgg19 import preprocess_input, decode_predictions
        print('Now Loading...')
        model_VGG19 = keras.models.load_model('vgg19_pretrain.h5')
        model_VGG19.summary()

    def onButtonClick4(self):  # 5-3 Show Data Augmentation
        import PIL.Image as Image
        import os
        import torchvision
        import matplotlib.pyplot as plt
        import numpy as np
        import warnings
        from torchvision import transforms
        from torchvision.transforms import functional as TF
        print('Now Loading...')
        imagepath = self.img
        warnings.filterwarnings("ignore")
        os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"
        # read image with PIL module
        img_pil = Image.open(imagepath, mode='r')

        # RandomRotation

        transform3 = transforms.Compose([
            transforms.RandomRotation(
                30, resample=Image.BICUBIC, expand=False, center=(55, 5))
        ])
        new_img3 = transform3(img_pil)
        img_np = np.asarray(new_img3)

        # RandomResizedCrop
        transform2 = transforms.RandomResizedCrop(size=(300, 300), scale=(0.08,
                                                                          1.0), ratio=(0.75, 1.3333333333333333), interpolation=2)

        new_img2 = transform2(img_pil)

        img_np = np.asarray(new_img2)

        # RandomVerticalFlip
        transform = transforms.Compose([
            transforms.Resize((300, 300)),
            transforms.RandomVerticalFlip(p=1),  # 機率
        ])

        new_img = transform(img_pil)
        img_np = np.asarray(new_img)

        axs = plt.figure().subplots(1, 3)
        axs[0].imshow(new_img3)
        axs[0].set_title('RandomRotation')
        axs[0].axis('off')
        axs[1].imshow(new_img2)
        axs[1].set_title('RandomResizedCrop')
        axs[1].axis('off')
        axs[2].imshow(new_img)
        axs[2].set_title('RandomVerticalFlip')
        axs[2].axis('off')
        plt.show()

    def onButtonClick5(self):  # 5-4 Show Accuracy And Loss
        img = cv2.imread('loss.jpg')
        cv2.imshow('loss and accuracy', img)
        cv2.waitKey(0)

    def onButtonClick6(self):  # 5-5 Inference
        import os
        import cv2
        import numpy as np
        from keras.applications.vgg19 import VGG19
        from keras.applications.vgg16 import VGG16
        import tensorflow
        from PIL import Image
        from tensorflow import keras
        from tensorflow.keras.preprocessing import image
        from tensorflow.keras.preprocessing.image import img_to_array
        from keras.applications.vgg19 import preprocess_input, decode_predictions
        print('Now Loading...')
        model_VGG19 = keras.models.load_model('vgg19_pretrain.h5')
        img_path = self.img
        # 将图像转换为网络需要的大小，因为我们这里加载的模型都是固定输入大小224*224
        img = image.load_img(img_path, target_size=(32, 32))
        # 首先需要转换为向量的形式
        img = image.img_to_array(img)
        # 扩充维度
        img = np.expand_dims(img, axis=0)
        # 对输入的图像进行处理
        img_out = preprocess_input(img)
        # decode the results into a list of tuples (class, description, probability)
        # (one such list for each sample in the batch)
        # 上面这段话的意思是输出包括（类别，图像描述，输出概率）
        preds = model_VGG19.predict(img_out)
        # 输出前三个结果的可能性
        # print(preds)
        classes = ['airplane', 'automobile', 'bird', 'cat',
                   'deer', 'dog', 'frog', 'horse', 'ship', 'truck']
        pred = np.argmax(preds, axis=1)

        # print the label of the class with maximum score
        print('Predicted Label:', classes[pred[0]])
        print('Confidence', np.max(preds))
        self.label.setText(classes[pred[0]])
        self.label.setFont(QFont('Arial', 20))
        self.label_4.setText(str(np.max(preds)))
        self.label_4.setFont(QFont('Arial', 10))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
