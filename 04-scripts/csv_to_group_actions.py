import csv

# Map roles to Google Groups (example)
ROLE_TO_GROUPS = {
    "media_contributor": ["gws-sd-media-contributors"],
    "media_viewer": ["gws-sd-media-viewers"],
}

def main(csv_path: str) -> None:
    with open(csv_path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            email = row["email"].strip()
            role = row["role"].strip()

            groups = ROLE_TO_GROUPS.get(role, [])
            if not groups:
                print(f"SKIP {email} (unknown role: {role})")
                continue

            for group in groups:
                # This prints the "action plan". In real life you could replace
                # this with Google Admin SDK / Directory API calls.
                print(f"ADD {email} -> {group}")

if __name__ == "__main__":
    main("sample_users.csv")
