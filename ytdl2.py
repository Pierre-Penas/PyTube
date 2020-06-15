from __future__ import unicode_literals
import youtube_dl
import os
from plyer import notification
print("Welcome in PyTube")

noms=[]
types=[]
while 1:
    a=input("name : (to skype, press enter) : ")
    if a == "":
        print("OK")
        break
    b=input("type (mp3 or mp4) : ")
    noms.append(a)
    types.append(b)
print("Download will begin.")
for x in noms:
    print("{}...".format(x))
    if types[noms.index(x)]=="mp4":
        ydl_opts = {"format":"best","outtmpl":"C:/Users/Utilisateur/Videos/{}.mp4".format(x)}
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download(['ytsearch:{}'.format(x)])
        print("OK")
    else:
        ydl_opts = {"format":"bestaudio","outtmpl":"C:/Users/Utilisateur/Music/{}.m4a".format(x)}
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download(['ytsearch:{}'.format(x)])
        print("OK")
end=notification.notify(title='Finished', message='Thanks for using PyTube', app_name='PyTube', app_icon="youtube.ico", timeout=5, ticker='', toast=False)
