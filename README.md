# Gesture-Recognition-Web-app

[![Language](https://img.shields.io/badge/Language-Python-yellow.svg?style=for-the-badge)](https://en.wikipedia.org/wiki/Programming_language)

This project is a web application designed for **real-time gesture recognition**. Using computer vision and machine learning, it processes live video input (e.g., from a webcam) to detect and classify gestures, displaying results through an interactive web interface.

## 📑 Table of Contents

- [Features](#features)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## 🚀 Features

- Real-time gesture recognition using a webcam  
- Detection of hand or body gestures using computer vision  
- User-friendly web interface built with Streamlit  
- Potential for training and recognizing custom gesture classes  
- Optional speech output for recognized gestures using `gTTS`  
- Visual feedback and result display via webcam overlay  

## 🧰 Technologies Used

- **Python**
- [OpenCV](https://pypi.org/project/opencv-python/)
- [Streamlit](https://streamlit.io/)
- [cvzone](https://github.com/cvzone/cvzone)
- [Pillow (PIL)](https://pillow.readthedocs.io/en/stable/)
- [MediaPipe](https://google.github.io/mediapipe/)
- [TensorFlow](https://www.tensorflow.org/)
- [gTTS](https://pypi.org/project/gTTS/) (Google Text-to-Speech)

## 🔧 Installation

Follow these steps to set up and run the project locally:

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/gesture-recognition-web-app.git
   cd gesture-recognition-web-app
   ```

2. **Install dependencies using pip:**
   ```bash
   pip install -r requirements.txt
   ```

   > Make sure Python 3.7 or higher is installed.

## ▶️ Usage

To run the web application:

1. Open a terminal in the project root directory.

2. Launch the Streamlit app:
   ```bash
   streamlit run app.py
   ```
   > If `app.py` isn't the main file, try:
   ```bash
   streamlit run app1.py
   ```

3. A browser window will open at [http://localhost:8501](http://localhost:8501). You can now interact with the gesture recognition interface.

4. Ensure the webcam is connected and accessible. If the application requires a trained model:
   - Check for a `Model/` directory.
   - If a script like `sign_language_training.py` exists, run it first to generate the model.

## 🧠 Model Training (Optional)

If you want to train a custom model:

1. Explore and customize `sign_language_training.py` or similar script.
2. Collect gesture images in folders labeled by class.
3. Train the model and export it to the `Model/` directory for use with the web app.

## 🤝 Contributing

Contributions are welcome!

1. Fork the repository  
2. Create a new feature branch:  
   ```bash
   git checkout -b feature/YourFeature
   ```
3. Commit your changes:  
   ```bash
   git commit -m "Add YourFeature"
   ```
4. Push to your branch:  
   ```bash
   git push origin feature/YourFeature
   ```
5. Open a Pull Request

