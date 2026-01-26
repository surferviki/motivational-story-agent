import time
from story_generator import generate_story, save_story

def main():
    story = generate_story()
    print("\n🌟 Your Motivational Story 🌟\n")
    print(story)

    save_story(story)

    # Keep the container alive for 1 minute so logs are visible
    print("\n⏳ Keeping container alive for 60 seconds...")
    time.sleep(60)

if __name__ == "__main__":
    main()
