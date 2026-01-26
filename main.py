import time
from story_generator import generate_story, save_story, send_whatsapp

def main():
    story = generate_story()
    print("\n🌟 Your Motivational Story 🌟\n")
    print(story)

    save_story(story)

    send_whatsapp(story)

    # Keep the container alive 60 seconds so we can see logs
    print("\n⏳ Keeping container alive for 60 seconds...")
    time.sleep(60)

if __name__ == "__main__":
    main()
