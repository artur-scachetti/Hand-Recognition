import cv2
import mediapipe as mp
import numpy as np
import math
from GameRect import DragRect

class Hand_Controler():

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


    def drag_and_drop(self, frame, lm_list):
        if not lm_list: 
            
            self.draw_rects(frame)
            return

        cursor = lm_list[8][1:]

        ix, iy = lm_list[4][1], lm_list[4][2]         
        tx, ty = lm_list[8][1], lm_list[8][2]
 
        dist = math.hypot(ix - tx, iy - ty)

        is_grabbing = dist < 60

        if is_grabbing:
            cv2.circle(frame, (ix, iy), 10, (0, 255, 0), cv2.FILLED) 
        else:
            cv2.circle(frame, (ix, iy), 10, (255, 0, 255), cv2.FILLED)

        for rect in self.rects:
            rect.update(cursor, is_grabbing)

        self.draw_rects(frame)


    def draw_rects(self, frame, piece):

        for rect in self.rects:

            if rect.piece == 'O':
                cx, cy = rect.posCenter
                w, h = rect.size
                x1, y1 = cx - w //2, cy - h //2
                x2, y2 = cx + w //2, cy + h //2

                cv2.rectangle(frame, (x1, y1), (x2, y2), rect.color, cv2.FILLED)

                if not rect.isLocked:
                    cv2.rectangle(frame, (x1, y1), (x2, y2), (255, 255, 255), 2)

            elif rect.piece == 'L':
                cx, cy = rect.posCenter
                w, h = rect.size
                x1, y1 = cx - w //2, cy - h //2
                x2, y2 = cx - w //6, cy + h //2
                x3, y3 = cx - w //6, cy + h //6
                x4, y4 = cx + w //6, cy + h //2

                cv2.rectangle(frame, (x1, y1), (x2, y2), rect.color, cv2.FILLED)
                cv2.rectangle(frame, (x3, y3), (x4, y4), rect.color, cv2.FILLED)
                
                if not rect.isLocked:
                    cv2.line(frame, (x1, y1), (x3, y1), (255,255,255), 2)
                    cv2.line(frame, (x3, y1), (x3, y3), (255,255,255), 2)
                    cv2.line(frame, (x3, y3), (x4, y3), (255,255,255), 2)
                    cv2.line(frame, (x4, y3), (x4, y4), (255,255,255), 2)
                    cv2.line(frame, (x4, y4), (x1, y2), (255,255,255), 2)
                    cv2.line(frame, (x1, y2), (x1, y1), (255,255,255), 2)


            elif rect.piece == 'S':
                cx, cy = rect.posCenter
                w, h = rect.size
                x1, y1 = cx - w //6, cy - h //6
                x2, y2 = cx + w //2, cy + h //6
                x3, y3 = cx + w //6, cy + h //6
                x4, y4 = cx - w //2, cy + h //2

                cv2.rectangle(frame, (x1, y1), (x2, y2), rect.color, cv2.FILLED)
                cv2.rectangle(frame, (x3, y3), (x4, y4), rect.color, cv2.FILLED)
                
                if not rect.isLocked:
                    cv2.line(frame, (x1, y1), (x2, y1), (255,255,255), 2)
                    cv2.line(frame, (x2, y1), (x2, y2), (255,255,255), 2)
                    cv2.line(frame, (x2, y2), (x3, y3), (255,255,255), 2)
                    cv2.line(frame, (x3, y3), (x3, y4), (255,255,255), 2)
                    cv2.line(frame, (x3, y4), (x4, y4), (255,255,255), 2)
                    cv2.line(frame, (x4, y4), (x4, y3), (255,255,255), 2)
                    cv2.line(frame, (x4, y3), (x1, y3), (255,255,255), 2)
                    cv2.line(frame, (x1, y3), (x1, y1), (255,255,255), 2)

            elif rect.piece == 'T':
                cx, cy = rect.posCenter
                w, h = rect.size
                x1, y1 = cx - w //6, cy - h //6
                x2, y2 = cx + w //6, cy + h //2
                x3, y3 = cx + w //2, cy + h //2
                x4, y4 = cx - w //2, cy + h //6

                cv2.rectangle(frame, (x1, y1), (x2, y2), rect.color, cv2.FILLED)
                cv2.rectangle(frame, (x3, y3), (x4, y4), rect.color, cv2.FILLED)
                
                if not rect.isLocked:
                    cv2.line(frame, (x1, y1), (x2, y1), (255,255,255), 2)
                    cv2.line(frame, (x2, y1), (x2, y4), (255,255,255), 2)
                    cv2.line(frame, (x2, y4), (x3, y4), (255,255,255), 2)
                    cv2.line(frame, (x3, y4), (x3, y3), (255,255,255), 2)
                    cv2.line(frame, (x3, y3), (x4, y3), (255,255,255), 2)
                    cv2.line(frame, (x4, y3), (x4, y4), (255,255,255), 2)
                    cv2.line(frame, (x4, y4), (x1, y4), (255,255,255), 2)
                    cv2.line(frame, (x1, y4), (x1, y1), (255,255,255), 2)
                
                
            elif rect.piece == 'J':
                cx, cy = rect.posCenter
                w, h = rect.size
                x1, y1 = cx - w //2, cy - h //2
                x2, y2 = cx + w //6, cy - h //6
                x3, y3 = cx - w //6, cy - h //6
                x4, y4 = cx + w //2, cy + h //2

                cv2.rectangle(frame, (x1, y1), (x2, y2), rect.color, cv2.FILLED)
                cv2.rectangle(frame, (x3, y3), (x4, y4), rect.color, cv2.FILLED)
                
                if not rect.isLocked:
                    cv2.line(frame, (x1, y1), (x2, y1), (255,255,255), 2)
                    cv2.line(frame, (x2, y1), (x2, y2), (255,255,255), 2)
                    cv2.line(frame, (x2, y2), (x3, y3), (255,255,255), 2)
                    cv2.line(frame, (x3, y3), (x3, y4), (255,255,255), 2)
                    cv2.line(frame, (x3, y4), (x4, y4), (255,255,255), 2)
                    cv2.line(frame, (x4, y4), (x1, y1), (255,255,255), 2)


            elif rect.piece == 'Z':
                cx, cy = rect.posCenter
                w, h = rect.size
                x1, y1 = cx - w //2, cy - h //6
                x2, y2 = cx + w //6, cy + h //6
                x3, y3 = cx + w //2, cy + h //6
                x4, y4 = cx - w //6, cy + h //2

                cv2.rectangle(frame, (x1, y1), (x2, y2), rect.color, cv2.FILLED)
                cv2.rectangle(frame, (x3, y3), (x4, y4), rect.color, cv2.FILLED)
                
                if not rect.isLocked:
                    cv2.line(frame, (x1, y1), (x2, y1), (255,255,255), 2)
                    cv2.line(frame, (x2, y1), (x2, y2), (255,255,255), 2)
                    cv2.line(frame, (x2, y2), (x3, y3), (255,255,255), 2)
                    cv2.line(frame, (x3, y3), (x3, y4), (255,255,255), 2)
                    cv2.line(frame, (x3, y4), (x4, y4), (255,255,255), 2)
                    cv2.line(frame, (x4, y4), (x4, y3), (255,255,255), 2)
                    cv2.line(frame, (x4, y3), (x1, y3), (255,255,255), 2)
                    cv2.line(frame, (x1, y3), (x1, y1), (255,255,255), 2)

            else:
                cx, cy = rect.posCenter
                w, h = rect.size
                x1, y1 = cx - w //2, cy - h //2
                x2, y2 = cx + w //2, cy + h //2

                if not rect.isLocked:
                    cv2.rectangle(frame, (x1, y1), (x2, y2), rect.color, cv2.FILLED)
                    cv2.rectangle(frame, (x1, y1), (x2, y2), (255, 255, 255), 2)
                    