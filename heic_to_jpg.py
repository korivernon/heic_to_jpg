import Tkinter as tk
import os
import converter

master = tk.Tk()
tk.Label(master, text="Location to File").grid(row=0)
tk.Label(master, text="Length").grid(row=1)
tk.Label(master, text="Width").grid(row=2)

e1 = tk.Entry(master)
e3 = tk.Entry(master)
e4 = tk.Entry(master)

e1.grid(row=0, column=1)
e3.grid(row=1, column=1)
e4.grid(row=2, column=1)

def show_entry_fields():
    if e1.get() != "":
        call_converter(e1.get(), e3.get(), e4.get())
    print("Location to File: %s\nLength: %s\nWidth: %s" % (e1.get(), e3.get(), e4.get()))

def get_source_folder(location):
    '''
    :param location: this is the location of the file
    '''
    # IMG
    sourceFolder = None
    if not os.path.isdir(location):
        #in the event that this is not a directory
        sourceFolder = os.getcwd()
    elif os.path.isdir(location):
        sourceFolder = location
    return sourceFolder

def get_img(location):
    '''
    :param location: this is the location of the file
    '''
    print("get_img({})".format(location))
    if location.find(".") == -1:
        return "."
    if location.rfind("/") != -1:
        return location[location.rfind("/")+1::]
    else:
        return location

def call_converter(location, length = 640, width = 480):
    '''
    :param location: this is the location of the file that will be converted
    :param length: this is the length of photo
    :param width: this is the width of the photo
    '''
    if length == "":
        length = 640
    if width == "":
        width = 480
    sourceFolder = get_source_folder(location)
    img = get_img(location)
    print(img, length, width, sourceFolder)
    if img == ".":
        files = [f for f in os.listdir(sourceFolder) if f.endswith(".HEIC")]
        for fil in files:
            converter.open_image(fil, length, width, sourceFolder)



tk.Button(master, 
          text='Quit', 
          command=master.quit).grid(row=4, 
                                    column=0, 
                                    sticky=tk.W, 
                                    pady=4)
tk.Button(master, 
          text='Show', command=show_entry_fields).grid(row=4, 
                                                       column=1, 
                                                       sticky=tk.W, 
                                                       pady=4)
master.title("HEIC to JPG Converter")
tk.mainloop()

master.mainloop()