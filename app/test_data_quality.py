from pathlib import Path
from data_quality import validate_file
knowledge_base = Path("data/knowledge_base") 
known_hashes = set()
for file_path in knowledge_base.iterdir(): 
    if file_path.is_file(): 
        is_valid, errors, file_hash = validate_file(file_path, known_hashes)

        print(f"\nFile: {file_path.name}")

        if is_valid:
           print("Status: VALID")
           known_hashes.add(file_hash)
        else:
           print("Status: INVALID")
           print("Errors:", errors)
