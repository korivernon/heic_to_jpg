from PIL import Image
import sys
import os
from wand.image import Image
import math

def open_image(img, length = 640, width = 480, SourceFolder = os.getcwd(), TargetFolder = os.getcwd() + "/res"):
    '''
    Open an image then convert the image from HEIC to JPG format.

    You can pass in length, width, SourceFolder, and TargetFolder parameters. By default,
    the source folder will be set to the current working directory, and for the TargetFolder
    it will be set to "res".

    :param img: the local name of the image that you would like to convert
    :param length: the new length of the image that you want to convert
    :param SourceFolder: the absolute path of the location of where the image is that you would like to convert
    :param TatgetFolder: the absolute path of the location of where you would like the new images to be saved
    '''
    f = img
    SourceFile=SourceFolder + "/" + img
    TargetFile=TargetFolder + "/" + img.replace(".HEIC",".JPG")
    img=Image(filename=SourceFile)
    img.format='jpg'
    l, w = img.size
    factor = 0
    if l > w:
        factor = int(math.ceil(l/length)) + 1
        img.thumbnail(l/factor,w/factor)
    else:
        factor = int(math.ceil(w/width)) + 1
        img.thumbnail(l/factor,w/factor)
    print("Converting {} --> {} ({},{})".format(f,f.replace(".HEIC", ".JPG"),int(l/factor),int(w/factor))) # output the file that you're currently converting
    img.save(filename=TargetFile)
    img.close()

def main():
    argv = sys.argv
    length = 640
    width = 480
    ext = "res"
    if len(argv) <= 2:
        print("error: converter.py\n\tthere must be one parameter passed into the command line argument")
        sys.exit(1)
    if argv[-1] == ".":
        files = [f for f in os.listdir(os.getcwd()) if f.endswith(".HEIC")]
        for fil in files:
            open_image(fil)
    # elif "*" in argv[-1]:
    #     # in the event that there is a wildcard
    #     if argv[-1][-2::] == "/*":
    #         if os.path.exists(os.path.join(os.getcwd(), argv[-1][:-2:])): # try to join the path
    #             files = [f for f in os.listdir(os.path.join(os.getcwd(),argv[-1][:-2:])) if f.endswith(".HEIC")]
    #             for fil in files:
    #                 sourceFolder = os.path.join(os.getcwd(), argv[-1][:-2:])
    #                 open_image(fil, length, width, sourceFolder, sourceFolder + ext)
    #         elif os.path.exists(argv[-1][:-2:]):
    #             files = [f for f in os.listdir(os.path.joing(os.getcwd(), argv[-1][:-2:])) if f.endswith(".HEIC")]
    #             for fil in files:
    #                 sourceFolder = hello
    else:
        open_image(argv[-1])

if __name__ == "__main__":
    main()
