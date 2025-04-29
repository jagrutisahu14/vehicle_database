# Vehicle Database (SQLite3)

This repository contains a sample SQLite3 database file `vehicles.db` which is used to store vehicle and owner information, including multiple photo fields for facial and vehicle image data.

## 🔧 What I Have Done

- I created the database structure using SQLite3.
- Designed and built the `vehicles` table with the following fields:
  - Owner name, number plate (unique), vehicle type, model, and color.
  - BLOB fields to store:
    - Up to 3 owner face photos
    - Up to 6 vehicle photos
- The database is designed to work with a Python application where data is entered and stored in binary format.
- This structure allows image-based identification and record-keeping for each vehicle.

## 🤖 Future Integration (with Face Recognition)

- This database will be used in a full intelligent system.
- A YOLO-based face detection model will detect faces from live video.
- Detected faces will be matched against the face photos stored in the database.
- On a successful match, the system will retrieve and display:
  - Owner's name
  - Vehicle number plate
  - Vehicle model and color
- A second database will be added to store red-flagged vehicle records, such as:
  - Vehicles with missing or obstructed plates
  - Unidentified vehicles detected via face recognition

## 📁 Files in this Repository

- `vehicles.db` — SQLite database file containing the vehicle and owner data structure (created by me)
