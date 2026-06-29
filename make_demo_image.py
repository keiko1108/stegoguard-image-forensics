from pathlib import Path
import base64

mode = Path("lab_mode.txt").read_text(encoding="utf-8").strip().lower()

if mode not in ["clean", "suspicious"]:
    raise SystemExit("lab_mode.txt must contain either: clean or suspicious")

Path("images").mkdir(exist_ok=True)

# Small valid 16x16 PNG image.
png_data = base64.b64decode(
    "iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAAAHklEQVQ4jWNgYGD4z8BQDwAAAP//AwAI/AL+hc2rNAAAAABJRU5ErkJggg=="
)

if mode == "suspicious":
    png_data += b"\nFORTESTING: This is harmless demo hidden data for the StegoGuard lab.\n"

Path("images/student_image.png").write_bytes(png_data)

print(f"Created images/student_image.png in {mode} mode")
