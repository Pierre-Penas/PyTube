#youtube downloader GUI
#GUI for youtube-dl
from __future__ import unicode_literals
import sys
from PyQt5.QtWidgets import QLabel, QApplication, QDialog, QDialogButtonBox, QHBoxLayout, QVBoxLayout, QLineEdit, QRadioButton, QPushButton

import youtube_dl



class Dialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("PyTube")
        dlgLayout=QVBoxLayout()
        HBoxLayout=QHBoxLayout()
        mp3=QRadioButton("mp3")
        mp3.setChecked(True)
        self.format="bestaudio"
        self.e=".m4a"
        mp4=QRadioButton("mp4")
        HBoxLayout.addWidget(mp3)
        HBoxLayout.addWidget(mp4)
        self.medias=QLabel("names of the audios (coma-separated)")
        dlgLayout.addWidget(self.medias)
        self.noms = QLineEdit()
        dlgLayout.addWidget(self.noms)
        dlgLayout.addLayout(HBoxLayout)
        download=QPushButton("Download")
        dlgLayout.addWidget(download)
        mp4.toggled.connect(self.fmp4)
        mp3.toggled.connect(self.fmp3)
        download.clicked.connect(self.ok)
        self.setLayout(dlgLayout)
    def ok(self):
        txt=self.noms.text()
        self.noms.setReadOnly(True)
        txt=txt.split(",")
        for x in txt:
            ydl_opts = {"format":self.format,"outtmpl":"C:/Users/Utilisateur/Music/{}.{}".format(x,self.e)}
            with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                ydl.download(['ytsearch:{}'.format(x)])
        print("OK")
        sys.exit(0)
    def fmp4(self):
        self.medias.setText("names of the videos (coma-separated)")
        self.format="best"
        self.e="mp4"
    def fmp3(self):
        self.medias.setText("names of the audios (coma-separated)")
        self.format="bestaudio"
        self.e="m4a"
if __name__ == "__main__":
    app=QApplication(sys.argv)
    dlg=Dialog()
    dlg.show()
    sys.exit(app.exec())