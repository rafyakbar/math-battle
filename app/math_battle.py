import numpy as np
import cv2
from app.support.helper import Helper
from app.math_battle_menu import MathBattleMenu

class MathBattle:
    def __init__(self, frame):
        self.__window_height = Helper.getMonitorHeight()
        self.__window_width = Helper.getMonitorWidth()

        self.__initFrameVars(frame)

        self.__menu = MathBattleMenu(self.__frame, self.__window_width, self.__window_height)

    def __initFrameVars(self, frame):
        self.__frame = np.zeros_like(frame)
        self.__frame[:, :] = np.array([255, 255, 255])
        self.__frame = cv2.resize(
            self.__frame,
            (
                self.__window_width,
                self.__window_height
            )
        )

    def getRenderedFrame(self, frame):
        frame = cv2.resize(
            frame,
            (
                self.__window_width,
                self.__window_height
            )
        )
        frame = cv2.flip(frame, 1)

        return self.__menu.getRenderedFrame(frame)