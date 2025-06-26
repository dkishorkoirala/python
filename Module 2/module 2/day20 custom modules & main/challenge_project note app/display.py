from note import get_notes

def show_note():
    notes = get_notes()
    if not notes:
        print("\nNo Notes Yet!!")
    else:
        print("\nYour Notes:")
        for i, note in enumerate(notes, 1):
            print(f"{i}. {note}")

