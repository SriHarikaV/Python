from cryptography.fernet import Fernet
import os

# Function to generate a new encryption key
def generate_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)

# Function to load the encryption key
def load_key():
    if not os.path.exists("key.key"):
        generate_key()  # Generate a key if it doesn't exist
    with open("key.key", "rb") as file:
        key = file.read()
    return key

# Load or generate key
key = load_key()
fer = Fernet(key)

# Function to view stored passwords
def view():
    if not os.path.exists("password.txt"):  
        print("No saved passwords found.")
        return
    
    with open("password.txt", "r") as f:
        for line in f.readlines():  # Read all lines
            data = line.rstrip()
            if "|" in data:
                user, passw = data.split("|")
                try:
                    print("User:", user, "| Password:", fer.decrypt(passw.encode()).decode())
                except:
                    print(f"Error decrypting password for {user} (Corrupt data)")

# Function to add new passwords
def add():
    name = input("Account Name: ")
    pwd = input("Password: ")

    with open("password.txt", "a") as f:
        f.write(name + "|" + fer.encrypt(pwd.encode()).decode() + "\n")

# Main program loop
while True:
    mode = input("Would you like to add a new password or view existing ones? (view/add) Press 'q' to quit: ").lower()
    if mode == "q":
        break
    elif mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("Invalid mode. Please enter 'view' or 'add'.")
