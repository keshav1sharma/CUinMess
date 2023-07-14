# Face Recognition Attendance System

This project is an implementation of a face recognition attendance system using OpenCV and face_recognition library. The system captures video from a webcam, detects faces in real-time, and matches them with known faces to mark attendance. It also records the time of attendance in a CSV file.

## Features

- Real-time face detection and recognition
- Matching detected faces with known faces
- Marking attendance with date and time stamp
- Saving attendance records in a CSV file

## Installation

To run the project, follow these steps:

1. Clone the repository or download the project files.
2. Install the required dependencies:
   - OpenCV (`pip install opencv-python`)
   - face_recognition (`pip install face_recognition`)

## Usage

1. Prepare the Known Faces:
   - Create a directory named "KnownFaces" and place images of known individuals in it.
   - Name the images according to the respective individuals.

2. Run the Program:
   - Open the terminal or command prompt and navigate to the project directory.
   - Run the command `python main.py` to start the face recognition attendance system.

3. Face Recognition and Attendance Marking:
   - The webcam will open, and faces will be detected in real-time.
   - If a known face is detected, it will be matched with the known faces from the "KnownFaces" directory.
   - If a match is found, the person's name will be displayed on the video feed, and attendance will be marked with the current date and time in the "Attendance.csv" file.

4. Exit the Program:
   - Press the "Esc" key to close the program.

## Troubleshooting

- If the program encounters any issues with face detection or recognition, ensure the following:
  - The known faces in the "KnownFaces" directory have distinct and clear images.
  - The webcam is positioned properly and has good lighting conditions.
  - Adjust the parameters for face detection and recognition in the code to optimize results.

## Future Enhancements

- Add a graphical user interface (GUI) to enhance the user experience.
- Implement a database to store attendance records and provide additional functionalities like generating reports and statistics.
- Integrate the system with an access control system to automate attendance management in various environments.

## References

- OpenCV: [https://opencv.org/](https://opencv.org/)
- face_recognition library: [https://github.com/ageitgey/face_recognition](https://github.com/ageitgey/face_recognition)
