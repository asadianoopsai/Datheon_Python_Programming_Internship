Automated File Organizer & Cleanup Utility

Project Overview
The Automated File Organizer is a Python application that organizes files into categorized folders based on their file extensions. It helps users maintain a cleaner directory and makes files easier to locate.

Objectives
- Automatically organize files by extension.
- Create category folders when required.
- Prevent existing files from being overwritten.
- Handle common file and folder errors.
- Display a summary of the organization process.

Technologies Used
- Python 3
- `os` — operating-system utilities.
- `shutil` — file movement.
- `pathlib` — file paths and extensions.

Features
1. **Automatic Categorization:** Organizes images, documents, videos, audio files, Python files, archives, and other files.
2. **Folder Creation:** Creates category folders automatically.
3. **Duplicate Handling:** Renames files when a file with the same name already exists in the destination folder.
4. **Error Handling:** Handles common file-access and operating-system errors.
5. **Confirmation:** Asks for confirmation before moving files.
6. **Summary Report:** Displays the number of files organized, skipped, and affected by errors.

Project Structure
text
Project-3-File-Organizer/
─ file_organizer.py
── README.md


 How to Run

 Prerequisites
Install Python 3 on your computer.

 Instructions
1. Open a terminal in the project folder.
2. Run the following command:

bash
python file_organizer.py


3. Enter the full path of the folder you want to organize.
4. Review the path and type `yes` to confirm.
5. Check the category folders created inside the selected directory.

 Example

Before organization:

text
FileOrganizer-Test/
─ notes.txt
─ report.pdf
─ photo.jpg
─ program.py
`

After organization:

text
FileOrganizer-Test/
─ Documents/
   ─ notes.txt
   ─ report.pdf
─ Images/
   ─ photo.jpg
─ Python/
   ─ program.py


 Testing
The program was tested using a dedicated folder containing four sample files. All four files were organized into their expected categories.

 Safety Notes
- Test the program on a dedicated sample folder before using it on important files.
- The program moves files from the selected folder into category subfolders.
- Review the selected folder carefully before confirming.

 Limitations
- Files are categorized using their extensions rather than their actual contents.
- Unknown extensions are placed in the `Others` folder.
- The program does not automatically undo file movements.

 Author
Developed as part of the **Datheon Python Programming Internship**.

 License
Created for educational and internship purposes.