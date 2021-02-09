import tkinter as tk
from PIL import Image, ImageTk
from tkinter.filedialog import askopenfile
import PyPDF2

window = tk.Tk()

window.title("PDF to text converter")
canvas = tk.Canvas(window, width = 225, height = 225)
canvas.grid(columnspan=3, rowspan=3)

#logo

logo = Image.open("pfd.jpg")
logo = ImageTk.PhotoImage(logo)
logo_label = tk.Label(image=logo)
logo_label.image = logo
logo_label.grid(column=1, row=0)

#instructions
instructions = tk.Label(window, text='Select a pdf from your computer', font="Raleway")
instructions.grid(columnspan=3, column=0, row=1)

#filing
def open_file():
    browse_text.set("Loading...")
    file = askopenfile(parent=window, mode="rb", title='choose a file', filetype=[('Pdf file', '*.pdf')])
    if file:
        read_pdf = PyPDF2.PdfFileReader(file)
        page_text = read_pdf.getPage(0)
        page_content = page_text.extractText()

        text_box = tk.Text(window, height=10, width=50, padx=15, pady=15)
        text_box.insert(1.0,page_content)
        text_box.tag_configure("center", justify="center")
        text_box.tag_add("center" , 1.0, 'end')
        text_box.grid(column=1,row=3)


        browse_text.set('browse')

#browse button
browse_text = tk.StringVar()
browse_button = tk.Button(window, command=lambda:open_file(), textvariable=browse_text, font="Raleway", bg="#20bebe", fg="white", height=2, width=15)
browse_text.set("browse")
browse_button.grid(column=1, row=2)


canvas = tk.Canvas(window, width = 600, height = 250)
canvas.grid(columnspan=3)


window.mainloop()