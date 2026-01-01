# Real-Time Face Detection System 🎯

This project implements a **real-time face detection system** using **OpenCV** and a **Haar Cascade classifier**.  
It detects human faces from a live webcam feed and draws bounding boxes around detected faces.

---

## 🚀 Features
- Real-time face detection using webcam
- Uses OpenCV Haar Cascade classifier
- Fast and lightweight
- Beginner-friendly computer vision project

---

## 🛠️ Tech Stack
- Python 🐍
- OpenCV (cv2)
- Haar Cascade XML Model

---

## 📂 Project Structure
face_detection_system/
│
├── face-reco.py
├── haarcascade_frontal_face_default.xml
└── README.md

yaml
Copy code

---

## ▶️ How to Run

### 1️⃣ Install dependencies
```bash
pip install opencv-python
2️⃣ Run the program
bash
Copy code
python face-reco.py
3️⃣ Exit
Press ESC key to close the webcam window.

🧠 How It Works
Captures live video using webcam

Converts frames to grayscale

Detects faces using Haar Cascade

Draws rectangles around detected faces

📸 Output
Green bounding boxes appear around detected faces in real time.
