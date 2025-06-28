# Real-Time Spatial Object Tracker with ROS + LDS

A robotics perception pipeline to detect and track object positions using ROS, laser distance sensor (LDS), and camera data. Designed for TurtleBot and real-time navigation tasks.

## 🔍 Features
- Fuses LDS and camera data to detect object location/direction
- Pixel-to-coordinate conversion for 3D localization
- Achieves ~94% accuracy in object estimation tasks

## 🛠 Tech Stack
- Python
- ROS (Robot Operating System)
- OpenCV
- PCL (point cloud library)

## 📦 Setup
```bash
# In ROS workspace
cd catkin_ws/src
git clone https://github.com/abhayKashyap03/spacial_track.git
cd ../
catkin_make
```

## 🧪 Metrics
- Response latency: <200ms
- Estimation accuracy: 94%
