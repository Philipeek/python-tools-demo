def normalize_filename(name: str) -> str:
    return name.lower().replace(" ", "_")

if __name__ == "__main__":
    print(normalize_filename("My File Name.jpg"))
