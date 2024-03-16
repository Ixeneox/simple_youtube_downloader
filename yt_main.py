from tkinter import *
from pytube import YouTube

root=Tk()


root.geometry("500x200")
root.resizable(False,False)
root.title('yt downloader')
root.iconbitmap('1.ico')
var=IntVar()
def download_command():
    chose=var.get()
    user_link=inp.get()
    video_object=YouTube(user_link)

    
    if chose==0:
        video_stream=video_object.streams.get_by_itag(137)
        video_stream.download()
    elif chose==1:
        video_stream=video_object.streams.get_by_itag(22)
        video_stream.download()
    elif chose==2:
        video_stream=video_object.streams.get_by_itag(18)
        video_stream.download()
    elif chose==3:
        video_stream=video_object.streams.get_audio_only()
        video_stream.download(filename='audio.mp3')



lbl=Label(root,text="PLEASE PASTE THE LINK :")
lbl.grid(row=0,column=0 , padx=10 , pady=20)

inp=Entry(root)
inp.focus_set()
inp.grid(row=0,column=1,columnspan=1)

r1=Radiobutton(root,text="Mp4 1080P",variable=var,value=0)
r2=Radiobutton(root,text="Mp4 720p",variable=var,value=1)
r3=Radiobutton(root,text="Mp4 420p",variable=var,value=2)
r4=Radiobutton(root,text="Audio only",variable=var,value=3)


r1.grid(row=1,column=0, padx=5 , pady=10)
r2.grid(row=1,column=1)
r3.grid(row=1,column=2)
r4.grid(row=1,column=3)

btn=Button(root,text='DOWNLOAD',command=download_command)
btn.grid(row=2,columnspan=4 , pady=10)

root.mainloop()