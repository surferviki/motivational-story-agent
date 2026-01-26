from story_generator import generate_story, save_story, send_whatsapp

def main():
    story = generate_story()
    print("\n🌟 Your Motivational Story 🌟\n")
    print(story)

    save_story(story)
    send_whatsapp(story)

    print("✅ Job done. Exiting.")

if __name__ == "__main__":
    main()
