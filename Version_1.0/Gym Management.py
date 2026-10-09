import mysql.connector

# Function to establish a database connection
def connect_to_database():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="mithun",
        database="gym_management_db")


# Function to create the required database tables
def create_tables(connection):
    cursor = connection.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS gym_members (
        ID INT AUTO_INCREMENT PRIMARY KEY,
        Name VARCHAR(255),
        Age INT,
        Gender VARCHAR(10),
        Bodyweight FLOAT,
        BMI FLOAT,
        Membership_type VARCHAR(20)
    )
    ''')
    connection.commit()
    cursor.close()

# Function to view gym members
def view_gym_members(connection):
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM gym_members")
    members = cursor.fetchall()
    for member in members:
        print(f"ID: {member[0]}, Name: {member[1]}, Age: {member[2]}, Gender: {member[3]}, Bodyweight: {member[4]}, BMI: {member[5]}, Membership Type: {member[6]}")
    cursor.close()

# Function to add a new gym member
def add_gym_member(connection):
    name = input("Enter Name: ")
    age = int(input("Enter Age: "))
    gender = input("Enter Gender: ")
    bodyweight = float(input("Enter Bodyweight: "))
    bmi = float(input("Enter BMI: "))
    membership_type = input("Enter Membership Type(Yearly/Monthly/Daily pass): ")

    cursor = connection.cursor()
    cursor.execute("INSERT INTO gym_members (name, age, gender, bodyweight, bmi, membership_type) VALUES (%s, %s, %s, %s, %s, %s)",
                   (name, age, gender, bodyweight, bmi, membership_type))
    connection.commit()
    cursor.close()
    print("Gym member added successfully!")

# Function to delete a gym member
def delete_gym_member(connection, member_id):
    cursor = connection.cursor()
    cursor.execute("DELETE FROM gym_members WHERE id = %s", (member_id,))
    connection.commit()
    cursor.close()
    print("Gym member deleted successfully!")

def update_gym_member(connection, member_id):
    print("Update Gym Member Information:")
    name = input("Enter Name: ")
    age = int(input("Enter Age: "))
    gender = input("Enter Gender: ")
    bodyweight = float(input("Enter Bodyweight: "))
    bmi = float(input("Enter BMI: "))
    membership_type = input("Enter Membership Type: ")

    cursor = connection.cursor()
    cursor.execute("UPDATE gym_members SET name = %s, age = %s, gender = %s, bodyweight = %s, bmi = %s, membership_type = %s WHERE id = %s",
                   (name, age, gender, bodyweight, bmi, membership_type, member_id))
    connection.commit()
    cursor.close()
    print("Gym member information updated successfully!")

if __name__ == "__main__":
    connection = connect_to_database()
    create_tables(connection)

    while True:
        print("--------------------------------------------------------------------------------")
        print("================================== Main Menu: ==================================")
        print("→ 1. Management")
        print("→ 2. Membership")
        print("→ 3. Exit")
        print("--------------------------------------------------------------------------------")

        choice = int(input("Enter your choice number : "))

        if choice == 1:
            # Management Menu
            print("--------------------------------------------------------------------------------")
            print("Management Menu:")
            print("1. View Gym Members")
            print("2. Delete Gym Member")
            print("3. Back")
            print("4. Update")
            print("--------------------------------------------------------------------------------")

            management_choice = int(input("Enter your choice number : "))
            print("--------------------------------------------------------------------------------")

            if management_choice == 1:
                view_gym_members(connection)    
            elif management_choice == 2:
                member_id = int(input("Enter the ID of the member to delete : "))
                delete_gym_member(connection, member_id)
            elif management_choice == 3:
                continue
            elif management_choice == 4:
                member_id = int(input("Enter the ID of the member to update : "))
                update_gym_member(connection, member_id)

        elif choice == 2:
            # Membership Menu
            add_gym_member(connection)

        elif choice == 3:
            # Exit the program
            connection.close()
            print("Exiting the program!")
            print("--------------------------------------------------------------------------------")
            break

        else:
            print("Invalid choice. Please enter a valid option.")

