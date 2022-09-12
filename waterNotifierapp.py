import time
from plyer import notification
if __name__ == "__main__":
    notification.notify(
        title = "Please Drink Water !!",
        message = "By Drinking Water You will have less chance of having Dehydration of Water, So Please Drink Water Now",
        app_icon = "D:\Python Practice\icon.ico",
        timeout=10
    )
