from PIL import ImageTk, Image
from tkinter import *
from pytube import YouTube

window = Tk()
window.geometry("600x400")
window.iconbitmap('')
window.resizable(0, 0)
window.title("Nguyễn Bình Minh - 3120410325")
window.config(background="#FFCCFF")

Label(window, text="YouTube Download Video", font='arial 20 bold', foreground="#3F3F3F").pack()

download_entries = []  # Danh sách để lưu các cặp widget nhập URL và nút xóa tương ứng
link = StringVar() # tạo biến link gán chuỗi rỗng
output = StringVar()

def add_url_entry():
    new_entry = Entry(window, width=80, textvariable = link)
    new_entry.place(x=60, y=len(download_entries) * 0 + 90)
    delete_button = Button(window, text="Delete", command=lambda: delete_entry(new_entry, delete_button))
    delete_button.place(x=500, y=len(download_entries) * 30 + 90)
    download_entries.append((new_entry, delete_button))
    update_position()

def delete_entry(entry, button):
    entry.destroy()
    button.destroy()
    download_entries.remove((entry, button))
    update_position()

def update_position():

  label_height = 30 # khoảng cách ô url được sinh ra

  for entry, button in download_entries:
    index = download_entries.index((entry, button))
    entry.place(x=60, y=160 + index * label_height)
    button.place(x=500, y=160 + index * label_height)
    
  output_label.place(x=60, y=len(download_entries) * 30 + 160)
  output_path.place(x=60, y=len(download_entries) * 30 + 190)
  download_button.place(x=250, y=len(download_entries) * 30 + 220)

Button(window, text="Add URL", font=("Helvetica", 10), foreground="#FFFFFF", background="#4CAF50", padx=2, command=add_url_entry).place(x=60, y=50)

output_label = Label(window, text="Output Pass Here:", font=("Helvetica", 12), foreground="#3F3F3F")
output_label.place(x=60, y=160)

output_path = Entry(window, width=80, textvariable = output)
output_path.place(x=60, y=190)



def download_video(url, output_path):
    yt = YouTube(url)
    video = yt.streams.filter(progressive=True, file_extension='mp4').last()
    video.download(output_path)
    Label(window, text=f"Downloaded {yt.title}", font='arial 15').place(x=300, y=220)

def download_all():
    try:
        output = output_path.get()
        for entry, _ in download_entries:
            url = entry.get()
            download_video(url, output)
    except Exception as e:
        print("Error in download_all:", e)
def download_all(output_path, download_entries):
    try:
        output = output_path.get()
        for entry, _ in download_entries:
            url = entry.get()
            download_video(url, output)
    except Exception as e:
        print("Error in download_all:", e)

download_button = Button(window, text="Download All", font=("Helvetica", 12), foreground="#FFFFFF", background="#4CAF50", padx=2, command=lambda: download_all(output_path, download_entries))
download_button.place(x=250, y=220)

window.mainloop()
