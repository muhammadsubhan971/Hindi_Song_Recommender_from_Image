# import os
# import mimetypes
# import cv2
# import uuid
# import streamlit as st
# from google import generativeai as genai
# import pywhatkit as pw

# # Configure Gemini API
# def configure_api():
#     api_key = "AIzaSyBDkLcFKzE_T6r1E5XjbuXVaoW40Szn71s"  # Use your real key here
#     genai.configure(api_key=api_key)
#     return genai.GenerativeModel('gemini-2.0-flash')

# def capture_from_webcam():
#     """Capture a single image from webcam and return the file path."""
#     cam = cv2.VideoCapture(0)
#     if not cam.isOpened():
#         raise Exception("Could not open webcam.")

#     print("Press 'Space' to capture the image, or 'Esc' to cancel.")

#     while True:
#         ret, frame = cam.read()
#         if not ret:
#             print("Failed to grab frame.")
#             break
#         cv2.imshow("Camera Feed - Press 'Space' to capture", frame)

#         key = cv2.waitKey(1)
#         if key % 256 == 27:  # ESC pressed
#             print("Capture cancelled.")
#             cam.release()
#             cv2.destroyAllWindows()
#             return None
#         elif key % 256 == 32:  # SPACE pressed
#             filename = f"temp_{uuid.uuid4().hex[:8]}.jpg"
#             cv2.imwrite(filename, frame)
#             print(f"Image saved to {filename}")
#             cam.release()
#             cv2.destroyAllWindows()
#             return filename

#     cam.release()
#     cv2.destroyAllWindows()
#     return None

# def process_image(image_path, model):
#     mime_type, _ = mimetypes.guess_type(image_path)
#     if not mime_type:
#         mime_type = "image/jpeg"

#     with open(image_path, "rb") as img_file:
#         image_data = img_file.read()

#     response = model.generate_content(
#         [
#             {"mime_type": mime_type, "data": image_data},
#             """complete analyze the given picture pay attention any detail of picture and tell which hindi song is suitble according person in picture 
#             just give me the name of one hindi song according to peroson in pic and just give the name of song no other detail just name ."""
#         ]
#     )
#     return response.text.strip()

# # Streamlit UI
# st.set_page_config(page_title="Hindi Song Recommender", layout="centered")
# st.title("🎶 Song Recommender from Image")

# st.write("### Aap image kaise doge?")
# option = st.radio("Choose input method:", ["Upload Image", "Capture from Webcam"])

# model = configure_api()

# image_path = None
# if option == "Upload Image":
#     uploaded_file = st.file_uploader("Drag and drop your image here", type=["jpg", "jpeg", "png"])
#     if uploaded_file:
#         image_path = f"temp_{uuid.uuid4().hex[:8]}.jpg"
#         with open(image_path, "wb") as f:
#             f.write(uploaded_file.read())
#         st.image(image_path, caption="Uploaded Image", use_column_width=True)

# elif option == "Capture from Webcam":
#     if st.button("Capture Image from Webcam"):
#         image_path = capture_from_webcam()
#         if image_path:
#             st.image(image_path, caption="Captured Image")

# if image_path and st.button("Suggest Hindi Song"):
#     with st.spinner("Analyzing image and finding a song..."):
#         try:
#             suggested_song = process_image(image_path, model)
#             st.success(f"🎵 Suggested Hindi Song: {suggested_song}")
#             pw.playonyt(suggested_song)
#             st.info("Playing song on YouTube...")
#         except Exception as e:
#             st.error(f"Error: {e}")
import os
import mimetypes
import cv2
import uuid
import streamlit as st
from google import generativeai as genai
import pywhatkit as pw

# Configure Gemini API
def configure_api():
    api_key = "AIzaSyBDkLcFKzE_T6r1E5XjbuXVaoW40Szn71s"  # Use your real key here
    genai.configure(api_key=api_key)
    return genai.GenerativeModel('gemini-2.0-flash')

def capture_from_webcam():
    cam = cv2.VideoCapture(0)
    if not cam.isOpened():
        st.error("Could not open webcam.")
        return None

    st.info("Capturing image... Press SPACE to capture.")
    filename = "ahmad.jpg"
    while True:
        ret, frame = cam.read()
        if not ret:
            st.error("Failed to grab frame.")
            break

        cv2.imshow("Camera Feed - Press SPACE to capture", frame)
        key = cv2.waitKey(1)
        if key % 256 == 32:  # SPACE pressed
            cv2.imwrite(filename, frame)
            break
        elif key % 256 == 27:  # ESC
            break

    cam.release()
    cv2.destroyAllWindows()
    if os.path.exists(filename):
        return filename
    return None

def process_image(image_path, model):
    mime_type, _ = mimetypes.guess_type(image_path)
    if not mime_type:
        mime_type = "image/jpeg"

    with open(image_path, "rb") as img_file:
        image_data = img_file.read()

    response = model.generate_content(
        [
            {"mime_type": mime_type, "data": image_data},
            """complete analyze the given picture pay attention any detail of picture and tell which pakistani song is suitble according person in picture 
            just give me the name of one hindi song according to peroson in pic and just give the name of song no other detail just name ."""
        ]
    )
    return response.text.strip()

# Streamlit UI
st.set_page_config(page_title="Hindi Song Recommender", layout="centered")
st.title("🎶 Hindi Song Recommender from Image")

st.write("### Aap image kaise doge?")
option = st.radio("Choose input method:", ["Upload Image", "Capture from Webcam"])

model = configure_api()

if option == "Upload Image":
    uploaded_file = st.file_uploader("Drag and drop your image here", type=["jpg", "jpeg", "png"])
    if uploaded_file:
        path = f"temp_{uuid.uuid4().hex[:8]}.jpg"
        with open(path, "wb") as f:
            f.write(uploaded_file.read())
        st.session_state.image_path = path
        st.image(path, caption="Uploaded Image", use_container_width=True)

elif option == "Capture from Webcam":
    if st.button("Capture Image from Webcam"):
        path = capture_from_webcam()
        if path:
            st.session_state.image_path = path
            st.image(path, caption="Captured Image", use_container_width=True)

if "image_path" in st.session_state and st.button("Suggest Hindi Song"):
    with st.spinner("Analyzing image and finding a song..."):
        try:
            suggested_song = process_image(st.session_state.image_path, model)
            st.success(f"🎵 Suggested Hindi Song: {suggested_song}")
            pw.playonyt(suggested_song)
            st.info("Playing song on YouTube...")
        except Exception as e:
            st.error(f"Error: {e}")
