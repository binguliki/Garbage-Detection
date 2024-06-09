import streamlit as st
from streamlit_webrtc import webrtc_streamer, VideoTransformerBase
import cv2
import numpy as np
from utils import MODEL

# CSS for the header style
html_for_head = """
    <style>
        .header {
            background-color: transparent;
            text-align: center;
            text-decoration: underline;
            text-decoration-style: solid;
            text-underline-offset: 5px;
            text-decoration-thickness: 1px;
            text-decoration-color: gold;
        }
    </style>
"""
st.markdown(html_for_head, unsafe_allow_html=True)
st.markdown("<h1 class ='header'>Garbage Detection Web App </h1>", unsafe_allow_html=True)

class VideoTransformer(VideoTransformerBase):
    def __init__(self):
        self.model = MODEL

    def transform(self, frame):
        img = frame.to_ndarray(format="bgr24")
        try:
            results = self.model.predict(img)
            
            for reff in results[0].boxes:
                box = reff.xywh[0]
                class_index = reff.cls[0]
                class_name = results[0].names[int(class_index)]
                if class_name == 'CARDBOARD':
                    continue
                
                font = cv2.FONT_HERSHEY_SIMPLEX
                font_scale = 0.7
                font_thickness = 2
                x, y, w, h = list(map(int, box))
                cv2.rectangle(img, (x - w // 2, y - h // 2), (x + w // 2, y + h // 2), (0, 0, 255), 2)
                cv2.putText(img, class_name, (x - w // 2, y - h // 2 - 5), font, font_scale, (0, 255, 0), font_thickness)
        except Exception as e:
            st.error(f"Error processing frame: {e}")
            return frame
        return img

webrtc_streamer(key='start', video_processor_factory=VideoTransformer)
