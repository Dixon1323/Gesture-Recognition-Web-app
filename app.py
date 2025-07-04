import cv2
import streamlit as st
from cvzone.HandTrackingModule import HandDetector
from cvzone.ClassificationModule import Classifier
import numpy as np
import math
import pyttsx3
from PIL import Image
from time import sleep

# Initialize the TTS engine
engine = pyttsx3.init()
engine_busy = False  # Flag to track if the engine is busy

# Function to process each frame
def process_frame(img, detector, classifier, labels):
    global engine_busy
    imgOutput = img.copy()
    hands, img = detector.findHands(img)

    if hands:
        hand = hands[0]
        x, y, w, h = hand['bbox']

        offset = 20
        imgSize = 300

        imgCrop = img[y - offset:y + h + offset, x - offset:x + w + offset]

        # Check if imgCrop is empty (i.e., has no dimensions)
        if not imgCrop.size:
            # Handle the case where imgCrop is empty
            return imgOutput

        aspectRatio = h / w

        if aspectRatio > 1:
            k = imgSize / h
            wCal = math.ceil(k * w)
            imgResize = cv2.resize(imgCrop, (wCal, imgSize))
            imgResizeShape = imgResize.shape
            wGap = (300 - wCal) // 2
            imgWhite = np.ones((imgSize, imgSize, 3), np.uint8) * 255
            imgWhite[0:imgResizeShape[0], wGap:wCal + wGap] = imgResize
        else:
            k = imgSize / w
            hCal = math.ceil(k * h)
            imgResize = cv2.resize(imgCrop, (imgSize, hCal))
            imgResizeShape = imgResize.shape
            hGap = math.ceil((imgSize - hCal) // 2)
            imgWhite = np.ones((imgSize, imgSize, 3), np.uint8) * 255
            imgWhite[hGap:hCal + hGap, :] = imgResize

        prediction, index = classifier.getPrediction(imgWhite, draw=False)

        cv2.rectangle(imgOutput, (x - offset, y - offset - 50), (x - offset + 150, y - offset - 50 + 50), (255, 0, 255), cv2.FILLED)
        cv2.putText(imgOutput, labels[index], (x, y - 26), cv2.FONT_HERSHEY_COMPLEX, 1.5, (255, 255, 255), 2)
        cv2.rectangle(imgOutput, (x - offset, y - offset), (x + w + offset, y + h + offset), (255, 0, 255), 4)


        if not engine_busy:
            text_to_speak = labels[index]
            print("Text to speak:", text_to_speak)  # Debugging statement
            engine.say(text_to_speak)
            engine_busy = True
            engine.runAndWait()
            engine_busy = False
            sleep(1)

    return imgOutput

# Main Streamlit app
def main():
    st.title("Sign Language Detection")
    st.markdown("""
    <style>
        .footer {
            position: fixed;
            bottom: 0;
            left: 0;
            width: 100%;
            background-color: #000000;
            text-align: center;
            padding: 5px;
        }
    </style>
    <div class="footer">
        S6 CSE MBITS
    </div>
""", unsafe_allow_html=True)

    cap = cv2.VideoCapture(0)
    detector = HandDetector(maxHands=1)
    classifier = Classifier("Model\keras_model.h5", "Model\labels.txt")

    labels = ["A", "B", "C", "D", "Heart", "Hello", "Thank You"]

    # Create a Streamlit placeholder to display the video
    video_placeholder = st.empty()

    while True:
        success, img = cap.read()
        img = process_frame(img, detector, classifier, labels)

        # Display the live video in the placeholder
        video_placeholder.image(img, channels="BGR", use_column_width=True, clamp=True)

        key = cv2.waitKey(1)
        if key & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
