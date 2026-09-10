# Automated Attendance System for Rural Schools (Prototype) 

An automated face-recognition attendance prototype developed as hands on practice based on past **Smart India Hackathon (SIH)** problem statements addressing rural education infrastructure.

Rural schools often face operational constraints, including unreliable high-speed internet, manual paper register inefficiencies, and proxy attendance. This prototype explores an offline first computer vision pipeline that logs student presence from a single classroom photograph into a standardized CSV record.

## Key Features

- **Multi-Face Recognition:** Processes group/classroom photos and matches faces against a local database using `DeepFace` paired with the `RetinaFace` detection backend.
- **Offline-First Execution:** Runs completely on local hardware without requiring continuous cloud connectivity, making it suitable for remote environments.
- **Automatic Deduplication:** Employs an in-memory hash set (`students_present`) to ensure students detected across multiple frames or angles are logged only once per run.
- **Structured CSV Logging:** Outputs clean, time-stamped attendance logs (`Name`, `Date`, `Time`) for straightforward integration with school record sheets or spreadsheet tools.

## Project Structure

```text
├── class_photo.jpeg          # Input group image / classroom photo
├── students_database/        # Directory containing reference student portraits
│   ├── student_one.jpg
│   └── student_two.jpg
├── attendance.csv            # Generated attendance output
├── main.py                   # Main detection and logging script
├── requirements.txt          # Project dependencies
└── README.md
