from GameEngine import GameEngine
import cv2

cap = cv2.VideoCapture('cap',0)
engine = GameEngine(cap)
engine.show_screen()
