import sqlite3

# Define the database file name
db_file = "vehicles.db"

def create_table():
    """Creates the 'vehicles' table in the database with multiple photo columns."""
    try:
        # Connect to the database (this will create the file if it doesn't exist)
        conn = sqlite3.connect(db_file)
        cursor = conn.cursor()

        # SQL command to create the table with multiple photo columns
        cursor.execute("""
            CREATE TABLE vehicles (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                owner_name TEXT,
                number_plate TEXT UNIQUE,
                vehicle_type TEXT,
                vehicle_model TEXT,
                colour TEXT,
                owner_face_photo1 BLOB,
                owner_face_photo2 BLOB,
                owner_face_photo3 BLOB,
                vehicle_photo1 BLOB,
                vehicle_photo2 BLOB,
                vehicle_photo3 BLOB,
                vehicle_photo4 BLOB,
                vehicle_photo5 BLOB,
                vehicle_photo6 BLOB
            )
        """)

        # Save the changes
        conn.commit()
        print(f"Table 'vehicles' created successfully in '{db_file}' with photo columns.")

    except sqlite3.Error as e:
        print(f"Error creating table: {e}")
    
    finally:
        # Close the connection
        if conn:
            conn.close()

def add_new_vehicle(owner,number_plate, vehicle_type, Vehicle_model, Vehicle_color,
                      owner_face_paths=None, vehicle_photo_paths=None):
    """Adds a new vehicle's information to the 'vehicles' table with multiple photos."""
    owner_face_data = [None] * 3
    vehicle_photo_data = [None] * 6

    if owner_face_paths:
        for i, path in enumerate(owner_face_paths[:3]):
            data = read_image_data(path)
            if data:
                owner_face_data[i] = data
                print(f"Owner face photo {i+1} read from: {path}")

    if vehicle_photo_paths:
        for i, path in enumerate(vehicle_photo_paths[:6]):
            data = read_image_data(path)
            if data:
                vehicle_photo_data[i] = data
                print(f"Vehicle photo {i+1} read from: {path}")

    try:
        # Connect to the database
        conn = sqlite3.connect(db_file)
        cursor = conn.cursor()

        # SQL command to insert data
        cursor.execute("""
            INSERT INTO vehicles (owner_name, number_plate, vehicle_type, vehicle_model, colour,
                                 owner_face_photo1, owner_face_photo2, owner_face_photo3,
                                 vehicle_photo1, vehicle_photo2, vehicle_photo3,
                                 vehicle_photo4, vehicle_photo5, vehicle_photo6)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (owner, number_plate, vehicle_type, Vehicle_model, Vehicle_color,
              owner_face_data[0], owner_face_data[1], owner_face_data[2],
              vehicle_photo_data[0], vehicle_photo_data[1], vehicle_photo_data[2],
              vehicle_photo_data[3], vehicle_photo_data[4], vehicle_photo_data[5]))

        # Save the changes
        conn.commit()
        print(f"Vehicle '{number_plate}' added successfully with photo data.")

    except sqlite3.IntegrityError:
        print(f"Error: Vehicle with number plate '{number_plate}' already exists.")
    except sqlite3.Error as e:
        print(f"Error adding vehicle: {e}")

    finally:
        # Close the connection
        if conn:
            conn.close()

def read_image_data(file_path):
    """Reads image data from the given file path in binary mode."""
    try:
        with open(file_path, 'rb') as file:
            return file.read()
    except FileNotFoundError:
        print(f"Error: File not found at {file_path}")
        return None

def main():
    # Create the table (it will only create if it doesn't exist)
    create_table()

    print("Ready to add vehicle information.")

    owner_name = input("Enter owner's name: ")
    number_plate = input("Enter vehicle number plate: ")
    vehicle_type = input("Enter vehicle type: ")
    vehicle_model = input("Enter vehicle model: ")
    colour = input("Enter vehicle colour: ")

    add_photo = input("Do you want to add owner and vehicle photos now? (yes/no): ").lower()

    owner_face_paths = []
    vehicle_photo_paths = []

    if add_photo == 'yes':
        print("Enter paths for owner's face photos (up to 3):")
        for i in range(1, 4):
            path = input(f"  Face photo {i} path (leave blank if none): ") or None
            if path:
                owner_face_paths.append(path)

        print("\nEnter paths for vehicle photos (up to 6):")
        for i in range(1, 7):
            path = input(f"  Vehicle photo {i} path (leave blank if none): ") or None
            if path:
                vehicle_photo_paths.append(path)

    # Add the new vehicle information
    add_new_vehicle(owner_name, number_plate, vehicle_type, vehicle_model, colour, owner_face_paths, vehicle_photo_paths)

    print("\nVehicle information added successfully.")

if __name__ == "__main__":
    main()