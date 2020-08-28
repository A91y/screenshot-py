from PIL import ImageGrab , Image
import datetime, time, os
from plyer import notification

# i = 0
# for i in range(100):
#     i = i + 1
#     break


hr = datetime.datetime.now().hour
mn = datetime.datetime.now().minute
sc = datetime.datetime.now().second
dy = datetime.datetime.now().day
mnt = datetime.datetime.now().month
yr = datetime.datetime.now().year  


def takeScreenshot():
    img = ImageGrab.grab()
    img.save(fp=f"IMG-{dy}{mnt}{yr}{hr}{mn}{sc}.png" , format="png")
    
path_cwd = os.getcwd()

# def hit(key):
#     pyautogui.press(key)
#     return
# char = sys.stdin.read(1)

if __name__ == "__main__":

    takeScreenshot()
    notification.notify(
        title = "ScreenShot Taken!!!",
        message = f"Image is saved as IMG-{dy}{mnt}{yr}{hr}{mn}{sc}.png",
        app_icon = os.path.join(path_cwd, "screenshot_icon.ico"),
        timeout = 3
    )
    






    # time.sleep(2)
    # while True:
    #     for event in pygame.event.get():
    #         if event.key == K_SPACE:
    # if hit("up"):
    # if pyautogui.hotkey("ctrlleft"):
    # if char = "ctrlleft":
    
    # print(char)

    # else:
    #     print("Invalid Key")
    

    # print(hr)
