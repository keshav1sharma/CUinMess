# CUinMess

This is a Python script that uses face recognition to mark attendance for students in a mess at Chitkara University. The script captures images from a webcam, compares them to a set of known faces, and marks attendance for any student members who are recognized.

Getting Started
To use this script, you will need to have Python 3.x installed on your computer, as well as the following libraries:

- OpenCV
- NumPy
- face_recognition
 You can install these libraries using pip:
 ```
 pip install opencv-python numpy face_recognition
```

Once you have installed the necessary libraries, you can run the script by navigating to the directory where the MessAttendance.py file is located and running the following command:

```
python MessAttendance.py
```
# Usage
When you run the script, it will open up a window showing the output from your webcam. The script will automatically detect any faces in the video stream and compare them to a set of known faces. If a match is found, the script will mark attendance for the corresponding staff member.

The attendance records are stored in a CSV file called Attendance.csv. Each record consists of the staff member's name and the time that they were recognized.

# Contributing
If you would like to contribute to this project, feel free to submit a pull request.


License
This project is licensed under the MIT License - see the LICENSE file for details.
