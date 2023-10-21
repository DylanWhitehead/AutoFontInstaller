from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QFileDialog, QLabel, QTreeWidget, QTreeWidgetItem, QStatusBar, QProgressBar, QHeaderView
from PyQt5.QtGui import QFont, QIcon
import sys
import os
import shutil

class FontInstallerApp(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(1000, 800)
        self.path = QLabel()
        self.initUI()

    def initUI(self):
        self.setStyleSheet(
            """
            QWidget {
                background-color: #ECEFF1;
                font-family: 'Roboto';
            }
            QPushButton {
                background-color: #03A9F4;
                color: #263238;
                border: none;
                padding: 10px;
                font-size: 16px;
                border-radius: 4px;
            }
            QPushButton:hover {
                background-color: #0288D1;
            }
            QLabel {
                color: #37474F;
                font-size: 16px;
            }
            QTreeWidget {
                background-color: #CFD8DC;
                border: 1px solid;
                border-color: #90A4AE;
                color: #37474F;
            }
            QStatusBar {
                color: #37474F;
            }
            QProgressBar {
                border: 2px solid grey;
                border-radius: 5px;
                color: #37474F;
                text-align: center;
            }
            """
        )

        layout = QVBoxLayout()
        file_layout = QHBoxLayout()
        info_layout = QVBoxLayout()
        info_text = QLabel('This app allows you to install fonts from a directory. Click on \'Browse\' to choose a directory, and then on \'Go\' to install the fonts.')
        info_text.setFont(QFont('Roboto', 18))

        self.tree = QTreeWidget()
        self.tree.setColumnCount(1)
        self.tree.setHeaderLabel("Files")

        self.processed = QTreeWidget()
        self.processed.setColumnCount(1)
        self.processed.setHeaderLabel("Processed Files")

        self.statusbar = QStatusBar()
        self.progressbar = QProgressBar()

        browseBtn = QPushButton('Browse', self)
        browseBtn.clicked.connect(self.showDialog)
        browseBtn.setWhatsThis("Click to select the folder from which the fonts will be installed.")

        goBtn = QPushButton('Go', self)
        goBtn.clicked.connect(self.installFonts)
        goBtn.setWhatsThis("Click to begin the font installation process.")

        file_layout.addWidget(self.path)
        file_layout.addWidget(browseBtn)

        info_layout.addWidget(info_text)

        layout.addLayout(info_layout)
        layout.addLayout(file_layout)
        layout.addWidget(self.tree)
        layout.addWidget(goBtn)
        layout.addWidget(self.processed)
        layout.addWidget(self.progressbar)
        layout.addWidget(self.statusbar)

        self.setLayout(layout)

        self.setWindowTitle('Font Installer')
        self.setWindowIcon(QIcon('./icon.png')) # add the path to your icon file 
        self.show()

    def showDialog(self):
        folder = QFileDialog.getExistingDirectory(self, 'Select Folder')
        if folder:
            self.folder_path = folder
            self.path.setText("Path: " + folder)
            self.init_tree()

    def init_tree(self):
        self.tree.clear()
        self.populate_tree(self.folder_path, self.tree.invisibleRootItem())

    def populate_tree(self, directory, parent_item):
        for path in os.scandir(directory):
            item = QTreeWidgetItem()
            item.setText(0, path.name)
            parent_item.addChild(item)
            if path.is_dir():
                self.populate_tree(path, item)

    def installFonts(self):
        self.processed.clear()
        total_files = len(list(os.walk(self.folder_path)))
        self.progressbar.setMaximum(total_files)
        progress_counter = 0

        for dirpath, dirnames, filenames in os.walk(self.folder_path):
            for filename in filenames:
                progress_counter += 1
                self.progressbar.setValue(progress_counter)
                if filename.endswith('.ttf') or filename.endswith('.otf'):
                    src = os.path.join(dirpath, filename)
                    dst = os.path.join('C:\\Windows\\Fonts', filename)
                    if not os.path.isfile(dst):
                        try:
                            shutil.copy(src, dst)
                            item = QTreeWidgetItem()
                            item.setText(0, f"Copied {filename} to Windows Fonts directory.")
                            self.processed.addTopLevelItem(item)
                        except PermissionError:
                            item = QTreeWidgetItem()
                            item.setText(0, f"Permission Denied: Could not copy {filename}. Please run as administrator.")
                            self.processed.addTopLevelItem(item)
                    else:
                        item = QTreeWidgetItem()
                        item.setText(0, f"Font {filename} already exists in Windows Fonts directory.")
                        self.processed.addTopLevelItem(item)

        self.progressbar.setValue(total_files)
        self.statusbar.showMessage("Font installation complete.")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = FontInstallerApp()
    sys.exit(app.exec_())