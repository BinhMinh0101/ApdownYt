from PIL import ImageTk, Image
from tkinter import *
from pytube import YouTube
window = Tk()
window.geometry("600x250") # set màn hình giao diện 
window.iconbitmap('')
window.resizable(0,0) # set tọa độ tiêu đề 0.0
window.title("Nguyễn Bình Minh - 3120410325")
window.config(background="#FFCCFF")

# photo = PhotoImage(file='C:\Users\Admin\Desktop\code\download yt\logo_yt.ico')
Label(window,text="YouTube Download Video", font = 'arial 20 bold', foreground="#3F3F3F").pack()
link = StringVar() # tạo biến link gán chuỗi rỗng
output = StringVar()
Label(window,text="Enter YouTube Video URL:", font=("Helvetica", 12), foreground="#3F3F3F").place(x= 60, y= 50)
link_enter = Entry(window,width = 80, textvariable = link).place(x= 60, y= 90)
Label(window, text = "Output Pass Here:", font=("Helvetica", 12), foreground="#3F3F3F").place(x= 60, y= 120)
output_path = Entry(window,width = 80, textvariable = output).place(x = 60, y=160)


def Downloaded():
    url = YouTube(str(link.get())) # truyền từ link sang dạng chuỗi
    video = url.streams.filter(progressive=True,file_extension='mp4').last() # lưu video mp4, với hàm last định dạng cao nhất, or fisrt là ngc lại
    video.download(str(output.get())) 
    Label(window, text = "Download", font ='arial 15').place(x = 300, y = 220)
Button(window, text = "Download", font=("Helvetica", 12), foreground="#FFFFFF",
       background="#4CAF50", padx=2, command= Downloaded).place(x =250, y = 200)
window.mainloop()
    