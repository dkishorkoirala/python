notes = []

def add_notes(n):
    notes.append(n)

def show_notes():
    if not notes:
        return "No notes yet"
    
    result = []
    for i, n in enumerate(notes):
        result.append(f"{i+1}. {n}")
    return "\n".join(result)