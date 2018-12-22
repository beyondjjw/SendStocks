from PIL import ImageGrab

def WindowCapture(filename):
    pic = ImageGrab.grab()
    pic.save(filename)