import ctypes
import cv2
import imutils

user32 = ctypes.windll.user32
user32.SetProcessDPIAware()

class Helper:
    @staticmethod
    def getMonitorWidth():
        return user32.GetSystemMetrics(0)

    @staticmethod
    def getMonitorHeight():
        return user32.GetSystemMetrics(1)

    @staticmethod
    def getObjectDetection(frame, lower_color, upper_color):
        image = frame.copy()

        # deteksi range warna dengan hsv
        converted = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
        mask = cv2.inRange(converted, lower_color, upper_color)

        # erosi dan dilasi
        mask = cv2.erode(mask, None, iterations=2)
        mask = cv2.dilate(mask, None, iterations=2)

        # mencari contour pada frame
        cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        cnts = cnts[0] if imutils.is_cv2() else cnts[1]

        # inislialisasi center objek
        center = None

        # jika menemukan minimal 1 contour
        if len(cnts) > 0:
            # mencari area terbesar
            max_area = max(cnts, key=cv2.contourArea)

            # mengambil jari-jari
            ((x, y), radius) = cv2.minEnclosingCircle(max_area)

            # moment dan center pada contour
            moment = cv2.moments(max_area)
            center = int(moment["m10"] / moment["m00"]), int(moment["m01"] / moment["m00"])

            return center, radius

        return None, None

    @staticmethod
    def isInRectangle(top, bottom, left, right, x, y):
        return top <= y and bottom >= y and left <= x and right >= x

