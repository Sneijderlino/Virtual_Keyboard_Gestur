import cv2
import winsound
import pyttsx3
from cvzone.HandTrackingModule import HandDetector

keys_layout = [
    list("1234567890"),
    list("QWERTYUIOP"),
    list("ASDFGHJKL;"),
    list("ZXCVBNM<>?")
]
special_keys = ["SHIFT", "SPACE", "ENTER", "DEL"]

detector = HandDetector(detectionCon=0.8, maxHands=1)
cap = cv2.VideoCapture(0)
cap.set(3,1280)
cap.set(4,720)

text_output = ""
shift_mode  = False
press_active = False

tts_engine = pyttsx3.init()
tts_engine.setProperty("rate", 180)
tts_engine.setProperty("volume", 1.0)

def play_beep():
    winsound.Beep(800, 100)

def speak_text(text):
    if text.strip():
        tts_engine.say(text.strip())
        tts_engine.runAndWait()

def draw_all(img, text, hover=None):
    h, w = img.shape[:2]
    overlay = img.copy()
    for i in range(h):
        c = int(40 + 100 * i / h)
        cv2.line(overlay, (0, i), (w, i), (c, 0, 150), 1)
    img = cv2.addWeighted(overlay, 0.4, img, 0.6, 0)

    for r, row in enumerate(keys_layout):
        for c2, key in enumerate(row):
            x, y = 100 + c2*110, 100 + r*110
            color = (0,255,120) if hover == key else (180,80,200)
            cv2.circle(img, (x, y), 48, (0,0,0), -1)
            cv2.circle(img, (x, y), 45, color, -1)
            cv2.putText(img, key, (x-20, y+15),
                        cv2.FONT_HERSHEY_SIMPLEX, 1.5, (255,255,255), 3)

    x0 = 100
    for sk in special_keys:
        color = (0,255,120) if hover == sk else (180,80,200)
        cv2.rectangle(img, (x0,550), (x0+180,620), (0,0,0), -1)
        cv2.rectangle(img, (x0,550), (x0+180,620), color, -1)
        cv2.putText(img, sk, (x0+15,600),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (255,255,255), 3)
        x0 += 200

    cv2.rectangle(img, (80,660), (1200,710), (200,150,255), 3)
    cv2.putText(img, text, (90,695),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (255,255,255), 2)
    return img

def hit_test(ix, iy):
    for r, row in enumerate(keys_layout):
        for c, key in enumerate(row):
            x, y = 100 + c*110, 100 + r*110
            if (ix - x)**2 + (iy - y)**2 <= 45**2:
                return key
    x0 = 100
    for sk in special_keys:
        if x0 < ix < x0+180 and 550 < iy < 620:
            return sk
        x0 += 200
    return None

while True:
    ret, img = cap.read()
    if not ret:
        break
    img = cv2.flip(img, 1)
    hands, img = detector.findHands(img, flipType=False)

    hover_key = None
    if hands:
        lm = hands[0]['lmList']
        tip_index  = lm[8]   
        tip_thumb  = lm[4]   

        cv2.circle(img, (tip_index[0], tip_index[1]), 10, (0,255,255), -1)
        hover_key = hit_test(tip_index[0], tip_index[1])


        dist = ((tip_index[0]-tip_thumb[0])**2 +
                (tip_index[1]-tip_thumb[1])**2) ** 0.5
        is_two_finger_click = (dist < 40) and hover_key is not None

        if is_two_finger_click and not press_active:
            if hover_key == "SPACE":
                text_output += " "
            elif hover_key == "ENTER":
                play_beep()
                speak_text(text_output)
            elif hover_key == "DEL":
                text_output = text_output[:-1]
            elif hover_key == "SHIFT":
                shift_mode = not shift_mode
            else:
                text_output += hover_key if shift_mode else hover_key.lower()

            play_beep()
            press_active = True

        if not is_two_finger_click:
            press_active = False

    img = draw_all(img, text_output, hover=hover_key)
    cv2.imshow("Virtual Keyboard", img)
    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()