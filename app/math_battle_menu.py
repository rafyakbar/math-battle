import cv2

class MathBattleMenu:
    def __init__(self, frame, window_width, window_height):
        self.__frame = frame
        self.__window_width = window_width
        self.__window_height = window_height

        self.__menu_button_distance = 25

        self.__menu_button_count = 3

        self.__menu_button_side = int((self.__window_width - ((self.__menu_button_count + 1) * self.__menu_button_distance)) / self.__menu_button_count)

        self.__title_box_position_top_left = (
            int(window_width / 4),
            0
        )
        self.__title_box_position_bottom_right = (
            int(self.__window_width / 4 * 3),
            int(self.__window_height / 8 * 1.2)
        )

        self.__title_position_buttom_left = (
            int(self.__window_width / 4 * 1.3),
            int(self.__window_height / 8 * 0.95)
        )

    def getRenderedFrame(self):
        # menggambar kotak nama tittle game
        cv2.rectangle(
            self.__frame,
            self.__title_box_position_top_left,
            self.__title_box_position_bottom_right,
            (0, 0, 0),
            5
        )

        # menggambar judul pada box
        cv2.putText(
            self.__frame,
            'MathBattle',
            self.__title_position_buttom_left,
            cv2.FONT_HERSHEY_SIMPLEX,
            3,
            (0, 0, 0),
            5
        )

        # menggambar tombol-tombol pada menu
        button_top_left_point_x = self.__menu_button_distance
        button_top_left_point_y = int(((self.__window_height - self.__title_box_position_bottom_right[1]) / 2))
        for c in range(0, self.__menu_button_count - 1):
            label = str(c + 1) + 'Player' + ('' if c == 0 else 's')
            self.__generateButton(button_top_left_point_x, button_top_left_point_y, label)
            button_top_left_point_x += self.__menu_button_side + self.__menu_button_distance
        self.__generateButton(button_top_left_point_x, button_top_left_point_y, 'Exit')

        return self.__frame

    def __generateButton(self, button_top_left_point_x, button_top_left_point_y, label):
        # menggambar tombol
        cv2.rectangle(
            self.__frame,
            (button_top_left_point_x, button_top_left_point_y),
            (button_top_left_point_x + self.__menu_button_side, button_top_left_point_y + self.__menu_button_side),
            (0, 0, 0),
            5
        )

        # menggambar text dalam tombol
        (label_width, label_height), baseline = cv2.getTextSize(
            label,
            cv2.FONT_HERSHEY_SIMPLEX,
            self.__menu_button_side * 0.007,
            5
        )
        text_point_x = int(button_top_left_point_x + ((self.__menu_button_side - label_width) / 2))
        text_point_y = int(button_top_left_point_y + ((self.__menu_button_side - label_height) / 2) + (label_height / 1.5))
        cv2.putText(
            self.__frame,
            label,
            (text_point_x, text_point_y),
            cv2.FONT_HERSHEY_SIMPLEX,
            self.__menu_button_side * 0.007,
            (0, 0, 0),
            5
        )