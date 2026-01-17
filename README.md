# Agusta CCTV Intruder Detection System

## 🔒 AI-Powered Smart Security Solution

Agusta is an intelligent CCTV surveillance system that uses AI to detect intruders while learning and recognizing regular visitors to prevent false alarms.

## 🌟 Features

### Core Functionality
- **Real-time Intruder Detection**: Monitors CCTV feeds in real-time to identify unauthorized persons
- **Smart Visitor Recognition**: Uses AI to learn and identify regular visitors (family members, staff, frequent guests)
- **Intelligent Alarm System**: Triggers alarms only for unknown/suspicious persons, eliminating false positives
- **Face Recognition Database**: Maintains a database of authorized visitors with timestamps
- **Multi-Camera Support**: Can handle multiple CCTV camera feeds simultaneously

### Advanced Features
- **Adaptive Learning**: Continuously improves recognition accuracy over time
- **Night Vision Support**: Works with infrared and low-light CCTV cameras
- **Motion Detection**: Pre-filters footage to analyze only when motion is detected
- **Alert Notifications**: Sends instant alerts via SMS, email, or mobile app
- **Activity Logging**: Records all detection events with timestamps and snapshots
- **Dashboard Interface**: Web-based control panel for monitoring and configuration

## 🛠️ Technology Stack

- **Programming Language**: Python 3.8+
- **AI/ML Framework**: TensorFlow / PyTorch
- **Face Recognition**: OpenCV, face_recognition library
- **Object Detection**: YOLO (You Only Look Once) or SSD
- **Backend**: Flask/FastAPI
- **Database**: SQLite/PostgreSQL
- **Video Processing**: OpenCV
- **Alarm System**: GPIO control (for hardware integration) or API-based notifications

## 📋 Requirements

```
Python >= 3.8
OpenCV >= 4.5
TensorFlow >= 2.0 or PyTorch >= 1.9
face-recognition >= 1.3
numpy >= 1.19
Flask >= 2.0
sqlite3 (built-in)
requests >= 2.26
pillow >= 8.0
```

## 🚀 Installation

### 1. Clone the Repository
```bash
git clone https://github.com/Lokihooda/Agusta-CCTV-Intruder-Detection.git
cd Agusta-CCTV-Intruder-Detection
```

### 2. Create Virtual Environment
```bash
python -m venv venv

# On Windows
venv\Scripts\activate

# On Linux/Mac
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure CCTV Connection
Edit `config.yaml` to add your CCTV camera details:
```yaml
cameras:
  - name: "Front Door"
    url: "rtsp://username:password@camera-ip:554/stream"
    type: "rtsp"
  - name: "Back Yard"
    url: "http://camera-ip/video.cgi"
    type: "http"
```

### 5. Run the Application
```bash
python main.py
```

## 📖 Usage

### Initial Setup
1. **Register Known Visitors**: Add photos of family members, staff, and regular visitors
```bash
python add_visitor.py --name "John Doe" --image path/to/photo.jpg
```

2. **Start Monitoring**:
```bash
python monitor.py
```

3. **Access Dashboard**: Open browser and navigate to `http://localhost:5000`

### Training the AI Model
```bash
python train_model.py --dataset data/visitors/
```

## 🎯 How It Works

1. **Video Stream Processing**: Captures frames from CCTV cameras (RTSP/USB/HTTP)
2. **Motion Detection**: Analyzes frames for movement to reduce processing load
3. **Face Detection**: Identifies human faces in the frame using Haar Cascades or MTCNN
4. **Face Recognition**: Compares detected faces against the known visitors database
5. **Decision Making**:
   - ✅ **Known Visitor**: Logs entry, no alarm
   - ⚠️ **Unknown Person**: Triggers alarm, sends notifications, saves snapshot
6. **Continuous Learning**: Optionally adds confirmed visitors to the database

## 🔧 Configuration

Edit `config.yaml` for customization:

```yaml
detection:
  confidence_threshold: 0.75
  unknown_threshold: 0.6
  frame_skip: 2
  
alarm:
  enabled: true
  notification_methods:
    - email
    - sms
    - push
  cooldown_seconds: 60

database:
  path: "data/visitors.db"
  
logging:
  save_snapshots: true
  snapshot_path: "data/snapshots/"
```

## 📁 Project Structure

```
Agusta-CCTV-Intruder-Detection/
│
├── main.py                 # Main application entry point
├── config.yaml            # Configuration file
├── requirements.txt       # Python dependencies
│
├── src/
│   ├── camera_handler.py  # CCTV connection and stream handling
│   ├── detector.py        # Face detection module
│   ├── recognizer.py      # Face recognition and matching
│   ├── alarm_system.py    # Alarm triggering and notifications
│   ├── database.py        # Visitor database management
│   └── utils.py           # Helper functions
│
├── models/
│   ├── face_detector/     # Pre-trained face detection models
│   └── face_recognizer/   # Trained face recognition models
│
├── data/
│   ├── visitors/          # Known visitor images
│   ├── snapshots/         # Captured intruder images
│   └── visitors.db        # SQLite database
│
├── web/
│   ├── app.py            # Flask web application
│   ├── templates/        # HTML templates
│   └── static/           # CSS, JS, images
│
└── tests/
    └── test_*.py         # Unit tests
```

## 🔐 Security & Privacy

- All visitor data is stored locally (no cloud upload by default)
- Encrypted database option available
- GDPR compliant data handling
- Option to auto-delete old snapshots
- Secure RTSP connection support

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 📧 Contact

**Project Maintainer**: Lokihooda  
**Email**: your.email@example.com  
**GitHub**: [@Lokihooda](https://github.com/Lokihooda)

## 🙏 Acknowledgments

- OpenCV community for computer vision tools
- face_recognition library by Adam Geitgey
- YOLO developers for object detection models
- TensorFlow/PyTorch teams for AI frameworks

## 🗺️ Roadmap

- [ ] Mobile app for iOS and Android
- [ ] Integration with smart home systems (Alexa, Google Home)
- [ ] Person tracking across multiple cameras
- [ ] Behavior analysis (loitering detection)
- [ ] Cloud backup option
- [ ] Advanced analytics dashboard
- [ ] Support for thermal cameras

---

**⭐ If you find this project useful, please consider giving it a star!**
