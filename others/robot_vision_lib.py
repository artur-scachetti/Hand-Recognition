import cv2
import mediapipe as mp
import numpy as np
import math

class Robot_Hands():

    def __init__(self):

        self.mp_hands = mp.solutions.hands
        self.mp_draw = mp.solutions.drawing_utils

        self.tips_id = [4, 8, 12, 16, 20]

        self.hands = self.mp_hands.Hands(
            max_num_hands=1, 
            min_detection_confidence =0.7,
            min_tracking_confidence=0.5
        )
    

    def get_hands_data(self, frame):

        h, w, _ = frame.shape

        self.frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        result = self.hands.process(self.frame_rgb)

        if result.multi_hand_landmarks:
            for hand_landmarks in result.multi_hand_landmarks:

                self.mp_draw.draw_landmarks(frame, hand_landmarks, self.mp_hands.HAND_CONNECTIONS)
                        
                lm_list = []
                for id, lm in enumerate(hand_landmarks.landmark):
                    cx, cy = int(lm.x * w), int(lm.y * h)
                    lm_list.append([id, cx, cy])
        
                return lm_list
    
    def get_finger_states(self, lm_list):
        if not lm_list: return []

        fingers = []

        if lm_list[self.tips_id[0]][1] < lm_list[self.tips_id[0] - 1][1]:
            fingers.append(1)

        else:
            fingers.append(0)
                
        for id in range(1,5):

            if lm_list[self.tips_id[id]][2] < lm_list[self.tips_id[id] - 1][2]:
                fingers.append(1)

            else:
                fingers.append(0)
                
        return fingers


    def hand_cmd(self, frame):

        lm_list = self.get_hands_data(frame)
        state = self.get_finger_states(lm_list)

        if state == [1, 1, 0,0,0]:

            self.bar_manipulate(frame, lm_list)

              
    def bar_manipulate(self, frame, lm_list):
            if not lm_list: return

            ix, iy = lm_list[4][1], lm_list[4][2]         
            tx, ty = lm_list[8][1], lm_list[8][2]
 
            dist = math.hypot(ix - tx, iy - ty)

            val_color= int(np.interp(dist, [50, 270], [0, 255]))
            color = (0, val_color, 255 - val_color)
                    
            bar_x, bar_y = 550, 50
            bar_w, bar_h = 35, 400

            bar_level = int(np.interp(dist, [50, 270], [bar_h, 0]))
            current_bar_y = int(bar_y + bar_level)

            cv2.rectangle(frame, (bar_x, bar_y), (bar_x + bar_w, bar_y + bar_h), color, 3)
            cv2.rectangle(frame, (bar_x, current_bar_y), (bar_x + bar_w, bar_y + bar_h), color, cv2.FILLED)

            print(f"{dist}")
    
    def show_frame(self):

        cap = cv2.VideoCapture(0)

        cap.set(3, 1280)
        cap.set(4, 720)

        if not cap.isOpened():
            print("Erro na câmera")
            return
        
        while True:

            ret, frame = cap.read()

            if not ret:
                print("Não foi possível capturar o frame")
                break

            frame  = cv2.flip(frame, 1)

            self.hand_cmd(frame)

            cv2.imshow("hands_detection", frame)

            if cv2.waitKey(1) == ord('q'):
                break

        cap.release()
        cv2.destroyAllWindows()

    def run(self):

        self.show_frame()