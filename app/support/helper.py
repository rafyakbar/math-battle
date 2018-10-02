import ctypes

user32 = ctypes.windll.user32
user32.SetProcessDPIAware()

class Helper:
    @staticmethod
    def getMonitorWidth():
        return user32.GetSystemMetrics(0)

    @staticmethod
    def getMonitorHeight():
        return user32.GetSystemMetrics(1)