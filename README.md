# 🗂️ Python CLI File Manager 

This repository contains a **Python CLI File Manager**

---

## 📌 Features of the CLI File Manager

- List files and directories (`ls`)
- Create files (`touch`)
- Create directories (`mkdir`)
- Remove files (`rm`)
- Remove directories (`rmdir`)
- Move/Rename files and directories (`mv`)
- View file contents (`cat`)

---

## 🔧 Installation

### 1️⃣ Clone the Repository
```sh
git clone https://github.com/your-username/python-file-manager.git
cd python-file-manager
```
### 2️⃣ Creating a File
```
python file_manager.py touch myfile.txt
```
Creates a new file named myfile.txt.
### 3️⃣ Creating a Directory
```
python file_manager.py mkdir my_folder
```
Creates a directory named my_folder.
### 4️⃣ Removing a File
```
python file_manager.py rm myfile.txt
```
Deletes myfile.txt.
### 5️⃣ Removing a Directory
```
python file_manager.py rmdir my_folder
```
Removes my_folder if empty.
### 6️⃣ Moving or Renaming Files
```
python file_manager.py mv oldname.txt newname.txt
```
Renames oldname.txt to newname.txt.
```
python file_manager.py mv myfile.txt my_folder/
```
Moves myfile.txt into my_folder/.
### 7️⃣ Viewing File Contents
```
python file_manager.py cat myfile.txt
Displays the content of myfile.txt.
```