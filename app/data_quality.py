from pathlib import Path
import hashlib

SUPPORTED_EXTENSIONS = {".txt", ".pdf"}
def calculate_file_hash(file_path): 
    hasher = hashlib.sha256()
    
    with open(file_path, "rb") as file:
        while True:
            chunk = file.read(4096)

            if not chunk:
                break

            hasher.update(chunk)

    return hasher.hexdigest()
def validate_file(file_path, known_hashes):
    file_path = Path(file_path)
    errors = []

    if not file_path.exists():
        errors.append("File does not exist.")
        return False, errors, None

    if file_path.suffix.lower() not in SUPPORTED_EXTENSIONS:
        errors.append("Unsupported file type.")

    if file_path.stat().st_size == 0:
        errors.append("File is empty.")

    if file_path.stat().st_size < 50:
        errors.append("File content is too short.")

    file_hash = calculate_file_hash(file_path)

    if file_hash in known_hashes:
        errors.append("Duplicate file detected.")

    is_valid = len(errors) == 0

    return is_valid, errors, file_hash
