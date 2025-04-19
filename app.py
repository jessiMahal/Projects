
import os

def create_file(filename):
    try:
        with open(filename, 'x') as f:
            print('Hello, welcome to my file!')
    except FileExistsError:
        print(f"File '{filename}' already exists.")
    except Exception as e:
        print(f"An error occurred: {e}")

def view_all_files():
    files = os.listdir()
    if not files:
        print("No files found.")
    else:
        print("Files in the current directory:")
        for file in files:
            print(file)

def delete_file(filename):
    try:
        os.remove(filename)
        print(f"File '{filename}' deleted successfully.")
    except FileNotFoundError:
        print(f"File '{filename}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

def edit_file(filename):
    try:
        with open(filename, 'a') as f:
            f.write('\nThis is an additional line.')
            print(f"File '{filename}' edited successfully.")
    except FileNotFoundError:
        print(f"File '{filename}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
        
def read_file(filename):
    try:
        with open(filename, 'r') as f:
            content = f.read()
            print(f"Content of '{filename}': {content}")
    except FileNotFoundError:
        print(f"File '{filename}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
    
    
def main():
    while True:
        print("\nMenu:")
        print("1. Create a file")
        print("2. View all files")
        print("3. Delete a file")
        print("4. Edit a file")
        print("5. Read a file")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            filename = input("Enter the filename to create: ")
            create_file(filename)
        elif choice == '2':
            view_all_files()
        elif choice == '3':
            filename = input("Enter the filename to delete: ")
            delete_file(filename)
        elif choice == '4':
            filename = input("Enter the filename to edit: ")
            edit_file(filename)
        elif choice == '5':
            filename = input("Enter the filename to read: ")
            read_file(filename)
        elif choice == '6':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")
    
if __name__ == "__main__":
    main()
        