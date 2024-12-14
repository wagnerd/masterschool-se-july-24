class MenuEntry():
    ID = 1
    def __init__(self, text: str, action: callable):
        self.text = text
        self.action = action
        self.id = MenuEntry.ID
        MenuEntry.ID += 1

    def run(self):
        self.action()

def action_1():
    print("I'm action 1")

def action_2():
    print("I'm action 2")

def show_menu(entries):
    for entry in entries:
        print(f"{entry.id}: {entry.text}")

    return int(input("What to do: "))

if __name__ == '__main__':
    entry_1 = MenuEntry("Entry text 1", action_1)
    entry_2 = MenuEntry("Entry text 2", action_2)

    entries = [entry_1, entry_2]

    entry_choice = show_menu(entries)
    # Run the entry by index
    entries[entry_choice - 1].run()
    # Run the entry based on ID
    for entry in entries:
        if entry.id == entry_choice:
            entry.run()
            break