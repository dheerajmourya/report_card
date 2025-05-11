import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
env_path = BASE_DIR / '.env'

print(f"Looking for: {env_path}")

if env_path.exists():
    print(".env found")
    with open(env_path) as f:
        for line in f:
            if line.strip() and not line.startswith("#"):
                key, value = line.strip().split("=", 1)
                os.environ[key] = value
else:
    print(".env not found")

print("SECRET_KEY =", os.environ.get("SECRET_KEY"))
print("DEBUG =", os.environ.get("DEBUG"))
print("ALLOWED_HOSTS =", os.environ.get("ALLOWED_HOSTS"))
