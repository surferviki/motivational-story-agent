from story_generator import generate_story, save_story, send_whatsapp

def main():
    # Generate a fun, motivational story
    story = generate_story()
    
    # Print it to logs for debugging
    print("\n🌟 Your Motivational Story 🌟\n")
    print(story)
    
    # Save story to a file
    save_story(story)
    
    # Send story via WhatsApp
    send_whatsapp(story)
    
    print("✅ Job done. Exiting.")

if __name__ == "__main__":
    main()
