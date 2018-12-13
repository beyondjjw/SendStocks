from PIL import ImageGrab

def window_capture(filename):
    pic = ImageGrab.grab()
    pic.save(filename)