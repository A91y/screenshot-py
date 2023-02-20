from PIL import ImageGrab , Image
import datetime, time, os
from plyer import notification

hr = datetime.datetime.now().hour
mn = datetime.datetime.now().minute
sc = datetime.datetime.now().second
dy = datetime.datetime.now().day
mnt = datetime.datetime.now().month
yr = datetime.datetime.now().year  

def takeScreenshot():
    img = ImageGrab.grab()
    img.save(fp=f"IMG-{dy}{mnt}{yr}{hr}{mn}{sc}.png" , format="png")
    
path_cwd = os.path.dirname(os.path.realpath(__file__))

if __name__ == "__main__":

    takeScreenshot()
    notification.notify(
        title = "ScreenShot Taken!!!",
        message = f"Image is saved as IMG-{dy}{mnt}{yr}{hr}{mn}{sc}.png",
        app_icon = os.path.join(path_cwd, "screenshot_icon.ico"),
        timeout = 3
    )
    
