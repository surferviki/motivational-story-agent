import os
from datetime import datetime
# Comment out OpenAI import for now
# from openai import OpenAI

# Mock client (not calling OpenAI)
# client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_story():
    # Mock story for testing
    story = (
        "Once upon a time, there was a small seed that wanted to grow into a big tree. "
        "Every day, it soaked up sunlight and drank water, even when storms came. "
        "The seed never gave up, and slowly it grew taller and stronger. "
        "One day, it became the tallest tree in the forest, giving shade and shelter to everyone. "
        "Remember, no matter how small you start, patience and effort will make you flourish!"
    )
    return story


def save_story(story):
    # Make a folder if it doesn't exist
    os.makedirs("stories", exist_ok=True)

    # File name with date
    today = datetime.now().strftime("%Y-%m-%d")
    filename = f"stories/story_{today}.txt"

    with open(filename, "w", encoding="utf-8") as f:
        f.write(story)

    print(f"💾 Story saved to {filename}")


if __name__ == "__main__":
    story = generate_story()
    print("\n🌟 Your Motivational Story 🌟\n")
    print(story)

    save_story(story)
