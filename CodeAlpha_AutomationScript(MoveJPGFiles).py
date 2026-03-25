import os
import shutil

# Set your folders here
source_folder = "source_folder"
destination_folder = "images_folder"

# Check if source folder exists
if not os.path.exists(source_folder):
    print("❌ Source folder does not exist!")
    exit()

# Create destination folder if not exists
os.makedirs(destination_folder, exist_ok=True)

# Supported image formats
image_extensions = (".jpg", ".jpeg", ".png")

moved_files = 0

for file in os.listdir(source_folder):
    file_path = os.path.join(source_folder, file)

    # Check if it's a file and has correct extension
    if os.path.isfile(file_path) and file.lower().endswith(image_extensions):
        
        destination_path = os.path.join(destination_folder, file)

        try:
            shutil.move(file_path, destination_path)
            print(f"✅ Moved: {file}")
            moved_files += 1
        except Exception as e:
            print(f"❌ Error moving {file}: {e}")

# Final output
if moved_files == 0:
    print("⚠️ No image files found in source folder.")
else:
    print(f"\n🎉 Total files moved: {moved_files}")