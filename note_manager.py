import os
import pickle

class Note:
    def __init__(self, title, content):
        self.title = title
        self.content = content

class NoteManager:
    def __init__(self, filename="notes.pkl"):
        self.filename = filename
        self.notes = []

        if os.path.exists(filename):
            with open(filename, "rb") as f:
                self.notes = pickle.load(f)

    def save_notes(self):
        with open(self.filename, "wb") as f:
            pickle.dump(self.notes, f)

    def create_note(self, title, content):
        note = Note(title, content)
        self.notes.append(note)
        self.save_notes()

    def read_notes(self):
        for idx, note in enumerate(self.notes, start=1):
            print(f"Note {idx} - {note.title}")

    def view_note(self, note_index):
        if 1 <= note_index <= len(self.notes):
            note = self.notes[note_index - 1]
            print(f"Title: {note.title}\nContent: {note.content}")

    def edit_note(self, note_index, new_title, new_content):
        if 1 <= note_index <= len(self.notes):
            self.notes[note_index - 1].title = new_title
            self.notes[note_index - 1].content = new_content
            self.save_notes()

    def delete_note(self, note_index):
        if 1 <= note_index <= len(self.notes):
            del self.notes[note_index - 1]
            self.save_notes()

def main():
    note_manager = NoteManager()

    while True:
        print("\nNote Manager Menu:")
        print("1. Create Note")
        print("2. Read Notes")
        print("3. View Note")
        print("4. Edit Note")
        print("5. Delete Note")
        print("6. Exit")

        choice = input("Select an option: ")

        if choice == "1":
            title = input("Enter note title: ")
            content = input("Enter note content: ")
            note_manager.create_note(title, content)
        elif choice == "2":
            note_manager.read_notes()
        elif choice == "3":
            note_manager.read_notes()
            note_index = int(input("Enter note number to view: "))
            note_manager.view_note(note_index)
        elif choice == "4":
            note_manager.read_notes()
            note_index = int(input("Enter note number to edit: "))
            new_title = input("Enter new title: ")
            new_content = input("Enter new content: ")
            note_manager.edit_note(note_index, new_title, new_content)
        elif choice == "5":
            note_manager.read_notes()
            note_index = int(input("Enter note number to delete: "))
            note_manager.delete_note(note_index)
        elif choice == "6":
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()