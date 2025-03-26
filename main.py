import os
import shutil
import argparse

def list_files():
    """Lists all files and directories in the current directory."""
    items = os.listdir('.')
    for item in items:
        print(f"📂 {item}" if os.path.isdir(item) else f"📄 {item}")

def create_file(filename):
    """Creates a new empty file."""
    with open(filename, 'w') as f:
        pass
    print(f"✅ File '{filename}' created.")

def create_directory(dirname):
    """Creates a new directory."""
    os.makedirs(dirname, exist_ok=True)
    print(f"✅ Directory '{dirname}' created.")

def delete_file(filename):
    """Deletes a file."""
    if os.path.exists(filename):
        os.remove(filename)
        print(f"❌ File '{filename}' deleted.")
    else:
        print(f"⚠️ File '{filename}' not found.")

def delete_directory(dirname):
    """Deletes a directory and its contents."""
    if os.path.exists(dirname):
        shutil.rmtree(dirname)
        print(f"❌ Directory '{dirname}' deleted.")
    else:
        print(f"⚠️ Directory '{dirname}' not found.")

def move_file(source, destination):
    """Moves a file or directory."""
    if os.path.exists(source):
        shutil.move(source, destination)
        print(f"📦 Moved '{source}' to '{destination}'.")
    else:
        print(f"⚠️ '{source}' not found.")

def read_file(filename):
    """Reads and prints the contents of a file."""
    if os.path.exists(filename):
        with open(filename, 'r') as f:
            print(f.read())
    else:
        print(f"⚠️ File '{filename}' not found.")

def main():
    parser = argparse.ArgumentParser(description="Simple Python CLI File Manager")
    parser.add_argument("command", help="Command to execute (ls, touch, mkdir, rm, rmdir, mv, cat)")
    parser.add_argument("args", nargs="*", help="Arguments for the command")

    args = parser.parse_args()

    command = args.command
    command_args = args.args

    if command == "ls":
        list_files()
    elif command == "touch" and command_args:
        create_file(command_args[0])
    elif command == "mkdir" and command_args:
        create_directory(command_args[0])
    elif command == "rm" and command_args:
        delete_file(command_args[0])
    elif command == "rmdir" and command_args:
        delete_directory(command_args[0])
    elif command == "mv" and len(command_args) == 2:
        move_file(command_args[0], command_args[1])
    elif command == "cat" and command_args:
        read_file(command_args[0])
    else:
        print("⚠️ Invalid command or missing arguments.")

if __name__ == "__main__":
    main()
