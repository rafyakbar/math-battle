from app.math_battle import MathBattle
import cv2

capture = cv2.VideoCapture(0)
ret, frame = capture.read()

mb = MathBattle(frame)

exit = False
while not exit:
    ret, frame = capture.read()

    cv2.namedWindow('', cv2.WND_PROP_FULLSCREEN)
    cv2.setWindowProperty('', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
    cv2.imshow('', mb.getRenderedFrame(frame))

    key = cv2.waitKey(1) & 0xFF
    if key == 27 or key == ord('q') or key == ord('Q'):
        exit = True