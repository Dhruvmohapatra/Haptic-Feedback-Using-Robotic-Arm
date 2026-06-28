# 🤖 Haptic Feedback Robotic Arm using Raspberry Pi & ESP32

![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge)
![ESP32](https://img.shields.io/badge/ESP32-Bluetooth-red?style=for-the-badge)
![Raspberry Pi](https://img.shields.io/badge/Raspberry%20Pi-4-green?style=for-the-badge)
![Arduino](https://img.shields.io/badge/Arduino-IDE-teal?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)

---

## 📌 Overview

This project presents a **gesture-controlled robotic arm** that mimics human finger movements using **flex sensors**, **ESP32**, and **Raspberry Pi**. The system also provides **haptic feedback** through a vibration motor, creating a more natural interaction between the user and the robotic arm.

The ESP32 collects flex sensor readings from a wearable glove and transmits them wirelessly via Bluetooth. The Raspberry Pi receives the sensor data, processes it, and controls the robotic arm using a PCA9685 servo driver.

---

# ✨ Features

- 🖐 Gesture-controlled robotic arm
- 📡 Bluetooth communication between ESP32 and Raspberry Pi
- 🤖 4-DOF robotic arm
- 🎯 Real-time finger movement tracking
- 📳 Haptic feedback using vibration motor
- ⚡ Low-latency wireless communication
- 🔧 Modular hardware design

---

# 🛠 Hardware Components

- Raspberry Pi 4
- ESP32 Development Board
- PCA9685 Servo Driver
- 4 × SG90 Servo Motors
- 3 × Flex Sensors
- Coin Vibration Motor
- Breadboard
- Jumper Wires
- 5V Power Supply

---

# 💻 Software Stack

- Python
- Embedded C++
- Arduino IDE
- Raspberry Pi OS
- Bluetooth Serial
- PyBluez
- Adafruit ServoKit

---

# 📂 Project Structure

```
Haptic-Feedback-Robotic-Arm
│
├── docs
│   └── Final_Report.pdf
│
├── esp32
│   ├── ESP32_Flex_BT.ino
│   └── Flex_Sensor_Test.ino
│
├── raspberry_pi
│   ├── bluetooth_receiver.py
│   ├── haptic_feedback.py
│   ├── servo_controller.py
│   ├── rfcomm-glove.service
│   └── permissions.txt
│
├── hardware
│   ├── components.md
│   └── pin_connections.md
│
├── images
│
├── requirements.txt
├── LICENSE
└── README.md
```

---

# 🔄 System Architecture

```
Flex Sensors
      │
      ▼
    ESP32
      │
 Bluetooth
      │
      ▼
 Raspberry Pi
      │
      ▼
 Servo Controller
      │
      ▼
 PCA9685 Driver
      │
      ▼
 SG90 Servo Motors
      │
      ▼
 Robotic Arm

      ▲
      │
Vibration Motor (Haptic Feedback)
```

---

# ⚙️ Working Principle

1. Flex sensors detect finger bending.
2. ESP32 reads analog sensor values.
3. Sensor values are transmitted to the Raspberry Pi using Bluetooth.
4. Raspberry Pi processes the received values.
5. Servo angles are calculated.
6. PCA9685 controls the servo motors.
7. Robotic arm replicates finger movement.
8. The vibration motor provides haptic feedback based on system logic.

---

# 📷 Project Images

## Smart Glove

> Add image here

```
images/glove.jpg
```

## Circuit Diagram

> Add image here

```
images/circuit_diagram.png
```

## Flowchart

> Add image here

```
images/flowchart.png
```

## Prototype

> Add image here

```
images/prototype.jpg
```

---

# 🚀 Installation

Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/Haptic-Feedback-Robotic-Arm.git
```

Go inside the project

```bash
cd Haptic-Feedback-Robotic-Arm
```

Install dependencies

```bash
pip install -r requirements.txt
```

Upload the ESP32 firmware using Arduino IDE.

Run the Raspberry Pi scripts.

---

# 📚 Libraries Used

- BluetoothSerial
- PyBluez
- RPi.GPIO
- Adafruit ServoKit
- NumPy

---

# 🔮 Future Improvements

- Machine Learning Gesture Recognition
- Computer Vision Integration
- Wi-Fi Based Communication
- Mobile Application
- Cloud Monitoring
- Force Sensor Based Haptic Feedback

---

# 📖 Documentation

The complete project report is available in:

```
docs/Final_Report.pdf
```

---

# 👨‍💻 Author

**Dhruv Mohapatra**

B.Tech Computer Science & Engineering (IoT)

Institute of Technical Education and Research (ITER)

SOA University, Bhubaneswar

---

# ⚠️ Note

This repository contains the recovered implementation of an academic project. Some source files were reconstructed after the original local project folder was accidentally lost. The overall architecture, hardware design, communication flow, and project documentation accurately reflect the implemented system.

---

# ⭐ If you found this project useful, consider giving it a star.