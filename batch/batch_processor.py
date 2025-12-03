import os

def process_folder(folder="input"):
    if not os.path.exists(folder):
        print("Folder not found:", folder)
        return

    for file in os.listdir(folder):
        print("Processing:", file)

if __name__ == "__main__":
    process_folder()
