
import json
import random
import sys
from pathlib import Path


# ==========================================
# CONTINUOUS STUDY STREAM
# ASSET GENERATOR
# ==========================================

BASE_DIR = Path(__file__).resolve().parent

MUSIC_DIRS = [
    BASE_DIR,
    BASE_DIR / "Lo-Fi",
    BASE_DIR / "music"
]

IMAGE_DIRS = [
    BASE_DIR / "Images",
    BASE_DIR / "images"
]


def find_music_files():

    music_files = []

    for folder in MUSIC_DIRS:

        if not folder.is_dir():
            continue

        music_files.extend(
            file for file in folder.iterdir()
            if file.is_file()
            and file.suffix.lower() == ".mp3"
        )

    # Remove duplicate paths
    music_files = list(set(music_files))

    if not music_files:
        raise FileNotFoundError(
            "No MP3 files found in repository root, "
            "Lo-Fi or music folder."
        )

    return music_files


def find_image_files():

    for folder in IMAGE_DIRS:

        if not folder.is_dir():
            continue

        images = [
            file for file in folder.iterdir()
            if file.is_file()
            and file.suffix.lower() in (
                ".jpg",
                ".jpeg",
                ".png"
            )
        ]

        if images:
            return images

    raise FileNotFoundError(
        "No JPG, JPEG or PNG images found "
        "inside Images or images folder."
    )


def get_quotes():

    facts = [
        "Silence is the best revenge.",
        "The eyes never lie, even when the lips do.",
        "Stay private, stay lowkey, stay happy.",
        "To gain power, learn to be unpredictable.",
        "Your biggest enemy is your own overthinking.",
        "Focus on your goals, not on distractions.",
        "Discipline creates freedom.",
        "Small progress is still progress.",
        "Your future needs your attention.",
        "Peace begins when comparison ends.",
        "Work hard in silence.",
        "Consistency beats temporary motivation.",
        "Protect your energy.",
        "Make your dreams bigger than your excuses.",
        "Be patient with your progress.",
        "Every day is a new opportunity.",
        "Stay focused and trust the process.",
        "Success starts with self-discipline.",
        "Less noise, more productivity.",
        "Believe in your own journey.",
        "Dream big, study hard.",
        "One page at a time.",
        "Your effort today builds your future.",
        "Stay calm and keep learning.",
        "Great things take time.",
        "Never stop improving yourself.",
        "Focus on progress, not perfection.",
        "Your dedication will pay off.",
        "Make today count.",
        "Learn something new every day."
    ]

    return random.sample(facts, 5)


def get_assets():

    music_files = find_music_files()
    image_files = find_image_files()

    selected_music = random.choice(music_files)
    selected_image = random.choice(image_files)

    return {
        "music": str(selected_music.relative_to(BASE_DIR)),
        "image": str(selected_image.relative_to(BASE_DIR)),
        "facts": get_quotes()
    }


# ==========================================
# MAIN
# ==========================================

if __name__ == "__main__":

    try:

        assets = get_assets()

        print(
            json.dumps(
                assets,
                ensure_ascii=False,
                indent=2
            )
        )

    except Exception as error:

        print(
            f"ASSET ERROR: {error}",
            file=sys.stderr
        )

        sys.exit(1)
