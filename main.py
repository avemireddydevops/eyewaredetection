import eyeglass_detector as detector
from datetime import datetime, timedelta
from time import sleep
import dlib, os
import ctypes  # An included library with Python install.


predictor_path = "./data/shape_predictor_5_face_landmarks.dat"
detector_method = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor(predictor_path)


def alert_message(msg):
    ctypes.windll.user32.MessageBoxW(
        0,
        msg,
        "Eye Care Alert",
        1,
    )


def control_PC(priority):
    if priority == 1:
        alert_message(
            "You are not wearing any spects. You will be logged out from your system now."
        )
        ctypes.windll.user32.LockWorkStation()
    elif priority == 2:
        # alert_message(
        #     "You are not wearing any spects. You will be logged out from your system now."
        # )
        os.system("shutdown /s /t 1")


# if not detector.detect_eyeglases(detector_method, predictor):
#     alert_message(
#         "You are not wearing any spects. We recomnend you to wear blue light filter spects for your eye care"
#     )

res = ""
count = 0
while True:

    dt = datetime.now()

    if not detector.detect_eyeglases(detector_method, predictor, 1):
        count += 1
        res += f"{count}"
        dt += timedelta(seconds=10)
        if res.endswith("1"):
            alert_message(
                "You are not wearing any spects. We recommend you to wear blue light filter spects for your eye care."
            )
        elif res.endswith("2"):
            alert_message(
                "You are not wearing any spects. Your PC will shutdown in 5mins. Please do wear spects inorder to keep the system alive."
            )
        elif res.endswith("3"):
            control_PC(1)
        elif res.endswith("4"):
            control_PC(2)
            count = 0

    else:
        res += "#"
        dt += timedelta(hours=1)

    print(res)
    while datetime.now() < dt:
        sleep(1)
