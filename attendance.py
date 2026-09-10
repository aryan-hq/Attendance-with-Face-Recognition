import csv
from datetime import datetime
import os
from deepface import DeepFace

print("Processing")

result = DeepFace.find(
    img_path="class_photo.jpeg", 
    db_path="students_database", 
    enforce_detection=False,
    detector_backend="retinaface"
)

students_present = set()

with open('attendance.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(["Name", "Date", "Time"])
    attendance_time = datetime.now().strftime("%H:%M:%S")
    attendance_date = datetime.now().strftime("%Y-%m-%d")

    for face_match in result:
        if not face_match.empty:
            
            matched_file_path = face_match.iloc[0]['identity']
            student_name = os.path.basename(matched_file_path).split('.')[0]
            
            if student_name not in students_present:
                students_present.add(student_name)
                writer.writerow([student_name, attendance_date, attendance_time])
                print(f"Present: {student_name}")

print(f"\nTotal students Present : {len(students_present)}")
print("\nAttendance stored in attendance.csv")