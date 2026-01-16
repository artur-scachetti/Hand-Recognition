import cv2
from HandController import Hand_Controler
import GameRect

class GameEngine:

    def __init__(self, cap):

        self.cap = cap

        self.border_p1 = (140, 110)
        self.border_p2 = (1140, 610)

        self.controller = Hand_Controler()

        self.rects = []
        self.rects.append(GameRect.Jpiece([500, 500]))

    def check_offside(self):
        pass

    def show_screen(self):
        
        while True:

            ret, frame = self.cap.read()
            frame  = cv2.flip(frame, 1)

            cv2.imshow('game', frame)

            lm_list = self.controller.get_hands_data(frame)
            self.controller.drag_and_drop(frame, lm_list)

            if cv2.waitKey(1) == ord('q'):
                break

        self.cap.release()
        cv2.destroyAllWindows()
