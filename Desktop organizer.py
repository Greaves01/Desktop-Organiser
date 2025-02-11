import os
import shutil

# Define the path to your desktop
desktop_path = os.path.expanduser("~/Desktop")

# Define categories for organizing files based on extensions
file_categories = {
    'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff'],
    'Documents': ['.pdf', '.doc', '.docx', '.txt', '.odt', '.rtf'],
    'Spreadsheets': ['.xls', '.xlsx', '.csv'],
    'Presentations': ['.ppt', '.pptx'],
    'Archives': ['.zip', '.rar', '.tar', '.tar.gz', '.7z'],
    'Audio': ['.mp3', '.wav', '.aac', '.flac'],
    'Videos': ['.mp4', '.mkv', '.avi', '.mov', '.flv'],
    'Code': ['.py', '.js', '.html', '.css', '.java'],
    'Executables': ['.exe', '.bat', '.sh', '.msi', '.lnk'],
    'Miscellaneous': []  # Any file that doesn't match other categories
}

# Function to create a folder if it doesn't exist
def create_folder(folder_name):
    folder_path = os.path.join(desktop_path, folder_name)
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

# Function to determine the category based on file extension
def get_file_category(file_extension):
    for category, extensions in file_categories.items():
        if file_extension.lower() in extensions:
            return category
    return 'Miscellaneous'  # If no category matches, put it in Miscellaneous

# Function to organize the desktop
def organize_desktop():
    # Get the list of all files and directories on the desktop
    for item in os.listdir(desktop_path):
        item_path = os.path.join(desktop_path, item)
        
        # If it's a file (not a directory), process it
        if os.path.isfile(item_path):
            # Get the file extension
            _, file_extension = os.path.splitext(item)
            category = get_file_category(file_extension)
            
            # Create category folder if it doesn't exist
            create_folder(category)
            
            # Move the file into the appropriate folder
            destination_path = os.path.join(desktop_path, category, item)
            try:
                shutil.move(item_path, destination_path)
                print(f"Moved: {item} -> {category}")
            except Exception as e:
                print(f"Failed to move {item}: {e}")
        else:
            # Skip directories (you can add additional handling for subdirectories if needed)
            print(f"Skipping directory: {item_path}")

# Run the desktop organizer
if __name__ == "__main__":
    print("Starting desktop organization...")
    organize_desktop()
    print("Desktop organization complete.")