class TechTalk:
    def __init__(self, title, date, time, description, speaker):
        self.title = title
        self.date = date
        self.time = time
        self.description = description
        self.speaker = speaker
        self.feedback = []

class Speaker:
    def __init__(self, name, bio):
        self.name = name
        self.bio = bio

class Attendee:
    def __init__(self, name):
        self.name = name
        self.registered_talks = []

def create_tech_talk():
    title = input("Enter tech talk title: ")
    date = input("Enter date (YYYY-MM-DD): ")
    time = input("Enter time (HH:MM): ")
    description = input("Enter description: ")
    speaker_name = input("Enter speaker's name: ")

    speaker = next((s for s in speakers if s.name == speaker_name), None)
    if not speaker:
        speaker_bio = input("Speaker not found. Enter bio: ")
        speaker = Speaker(speaker_name, speaker_bio)
        speakers.append(speaker)

    talk = TechTalk(title, date, time, description, speaker)
    tech_talks.append(talk)
    print("Tech talk created!")

def view_tech_talks():
    if not tech_talks:
        print("No tech talks scheduled.")
        return

    for i, talk in enumerate(tech_talks):
        print(f"{i + 1}. {talk.title} | {talk.date} | {talk.time} | Speaker: {talk.speaker.name}")

def delete_tech_talk():
    view_tech_talks()
    index = int(input("Enter the number of the tech talk to delete: ")) - 1
    if 0 <= index < len(tech_talks):
        del tech_talks[index]
        print("Tech talk deleted.")
    else:
        print("Invalid selection.")

def register_attendee():
    name = input("Enter your name: ")
    talk_title = input("Enter the title of the tech talk you want to attend: ")
    talk = next((t for t in tech_talks if t.title == talk_title), None)

    if talk:
        attendee = next((a for a in attendees if a.name == name), None)
        if not attendee:
            attendee = Attendee(name)
            attendees.append(attendee)
        attendee.registered_talks.append(talk)
        print(f"{name} registered for {talk_title}.")
    else:
        print("Tech talk not found.")

def recommend_tech_talks(employee_name):
    attendee = next((a for a in attendees if a.name == employee_name), None)
    if not attendee:
        print("Attendee not found.")
        return

    print("\nRecommended Tech Talks for you:")
    for talk in tech_talks:
        if talk not in attendee.registered_talks:
            print(f"- {talk.title} by {talk.speaker.name} on {talk.date} at {talk.time}")

def gather_feedback(talk):
    feedback = input("Enter your feedback for this tech talk: ")
    talk.feedback.append(feedback)
    print("Feedback submitted!")

def analyze_feedback(talk_id):
    if talk_id < 0 or talk_id >= len(tech_talks):
        print("Invalid tech talk ID.")
        return

    talk = tech_talks[talk_id]
    if not talk.feedback:
        print("No feedback available for this tech talk.")
        return

    print(f"\nFeedback for '{talk.title}':")
    for i, feedback in enumerate(talk.feedback, 1):
        print(f"{i}. {feedback}")

def main():
    while True:
        print("\n1. Create Tech Talk")
        print("2. View Tech Talks")
        print("3. Delete Tech Talk")
        print("4. Register Attendee")
        print("5. Recommend Tech Talks")
        print("6. Gather Feedback")
        print("7. Analyze Feedback")
        print("8. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            create_tech_talk()
        elif choice == '2':
            view_tech_talks()
        elif choice == '3':
            delete_tech_talk()
        elif choice == '4':
            register_attendee()
        elif choice == '5':
            employee_name = input("Enter your name to get recommendations: ")
            recommend_tech_talks(employee_name)
        elif choice == '6':
            view_tech_talks()
            talk_index = int(input("Enter the number of the tech talk to provide feedback: ")) - 1
            gather_feedback(tech_talks[talk_index])
        elif choice == '7':
            view_tech_talks()
            talk_index = int(input("Enter the number of the tech talk to analyze feedback: ")) - 1
            analyze_feedback(talk_index)
        elif choice == '8':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    tech_talks = []
    speakers = []
    attendees = []
    main()
