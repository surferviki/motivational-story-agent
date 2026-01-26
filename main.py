from story_generator import generate_story, save_story, send_whatsapp
import time

def main():
    story = generate_story()
    print("\n🌟 Your Motivational Story 🌟\n")
    print(story)

    save_story(story)
    send_whatsapp(story)

    print("\n⏳ Keeping container alive for 60 seconds...")
    time.sleep(60)

if __name__ == "__main__":
    main()
