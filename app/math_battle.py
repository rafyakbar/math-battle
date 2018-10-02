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
                Helper.getMonitorWidth(),
                int(((Helper.getMonitorWidth() - frame.shape[1]) / frame.shape[1] + 1) * frame.shape[0])
            )
        )

    def getRenderedFrame(self, frame):

        return self.__menu.getRenderedFrame()