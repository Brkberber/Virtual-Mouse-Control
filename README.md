# Virtual Mouse Control

Control your computer's mouse using **hand tracking with OpenCV and MediaPipe**.  
This project allows you to move the mouse cursor and perform clicks with finger gestures in real time using a standard webcam.  

---

## Features
- **Cursor control** using the index finger position  
- **Click gesture** by touching index and middle fingers together  
- **Smooth and responsive tracking**  
- **Frame boundary detection** to improve cursor accuracy  

---

## Requirements
Make sure you have the following dependencies installed:  
```bash
pip install opencv-python mediapipe numpy pyautogui
```

---

## How It Works
1. The webcam captures your hand using **OpenCV**.  
2. **MediaPipe** detects hand landmarks in real time.  
3. **Index finger controls the cursor** by mapping its position to the screen dimensions.  
4. **Click gesture** is detected when index and middle fingers come close together.  
5. **PyAutoGUI** moves the mouse and performs clicks.  

---

## Usage
1. Clone this repository:  
   ```bash
   git clone https://github.com/Brkberber/Virtual-Mouse-Control.git
   cd Virtual-Mouse-Control
   ```
2. Run the main script:  
   ```bash
   python main.py
   ```
3. Keep your hand inside the camera frame.  
   - **Move cursor:** Raise your index finger only.  
   - **Click:** Raise both index and middle fingers, then touch them together.  
4. Press **'q'** to quit.  

---

## File Structure
- **main.py** – Handles real-time hand detection and mouse control.  
- **HandTrackingModule.py** – Utility module for detecting hands, positions, and finger states.  

---

## Notes
- Adjust the `frameR` value for better boundary control depending on your camera.  
- Make sure to give camera access permission if prompted.  
- For best results, use in **well-lit environments**.  
