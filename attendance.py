import csv
from datetime import datetime
import os
from deepface import DeepFace

print("Analyzing the photo...")

results = DeepFace.find(
    img_path="class_photo.jpg", 
    db_path="students_database", 
    enforce_detection=False,
    detector_backend="retinaface"
)

marked_students = set()

with open('attendance.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(["Name", "Date", "Time"])
    attendance_time = datetime.now().strftime("%H:%M:%S")
    attendance_date = datetime.now().strftime("%Y-%m-%d")

    for face_match_data in results:
        if not face_match_data.empty:
            
            matched_file_path = face_match_data.iloc[0]['identity']
            student_name = os.path.basename(matched_file_path).split('.')[0]
            
            if student_name not in marked_students:
                marked_students.add(student_name)
                writer.writerow([student_name, attendance_date, attendance_time])
                print(f"Marked Present: {student_name}")
            else:
                print(f"Duplicate entry : {student_name}, skipping.")

print(f"\nTotal unique students : {len(marked_students)}")
print("\nAttendance stored in attendance.csv")