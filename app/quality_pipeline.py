from pathlib import Path
import shutil

from data_quality import validate_file


def run_quality_check(
	knowledge_base_path="data/knowledge_base",
	quarantine_path="data/quarantine",
):
    knowledge_base = Path(knowledge_base_path)
    quarantine = Path(quarantine_path)
    quarantine.mkdir(parents=True, exist_ok=True)

    known_hashes = set()

    for file_path in knowledge_base.iterdir():
        if not file_path.is_file():
            continue

        is_valid, errors, file_hash = validate_file(
            file_path,
            known_hashes
        )

        print(f"\nChecking: {file_path.name}")

        if is_valid:
            print("Status: VALID")
            known_hashes.add(file_hash)

        else:
            print("Status: INVALID")
            print("Errors:", errors)

            destination = quarantine / file_path.name

            shutil.move(
                str(file_path),
                str(destination)
            )

            print(
                f"Moved to quarantine: {destination}"
            )
if __name__ == "__main__":
    run_quality_check()