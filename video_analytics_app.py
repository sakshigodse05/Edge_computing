import streamlit as st
import cv2
from ultralytics import YOLO
import tempfile
import time

st.set_page_config(page_title="Real-Time Video Analytics", layout="centered")
st.title("📹 Real-Time Video Analytics Dashboard")

run_button = st.button("▶️ Start Video Feed")

if run_button:
    # Load YOLOv8 model (nano for speed)
    model = YOLO("yolov8n.pt")

    # Temporary space to display frames
    FRAME_WINDOW = st.image([])

    # Open webcam
    cap = cv2.VideoCapture(0)

    st.info("Press 'Stop' or close the window to end video feed.")

    stop_btn = st.button("⏹️ Stop", key="stop_button")

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret or stop_btn:
            break

        # Run YOLO detection
        results = model(frame)
        annotated = results[0].plot()

        # Convert from BGR (OpenCV) to RGB (Streamlit)
        FRAME_WINDOW.image(cv2.cvtColor(annotated, cv2.COLOR_BGR2RGB))

        time.sleep(0.05)  # Limit to ~20 FPS

    cap.release()
    st.success("🔚 Video Feed Stopped.")
