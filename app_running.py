# Challenge: Get the App Running

# The app has show_queue stubbed and the "quit" command wired up. 
# Two more functions need stubs, and the loop only handles "quit" so far.

# 1. Stub add_singer and remove_singer, following the show_queue example: each takes
#    queue, has a one-sentence docstring, and prints a placeholder like "[add a singer]".

# 2. Finish the if/elif/else chain. When the command is "add" or
#    "remove", call the matching function.

# 3. Add an else that handles when the app receives an unrecognized command (see the example below).

# 4. Call run_app(queue) and test it. Make sure add, remove, and quit each work, and that
#   typing a command that doesn't exist, like "sing", prints your message and doesn't
#   crash the app.

queue = [("Annie", "Dancing Queen"), ("Allen", "Country Roads")]

# prompt for singer

def prompt_for_singer():
    """Prompt the host for a singer's name and song."""
    name = input("Name: ").strip().title()
    song = input("Song: ").strip().title()
    return name, song

def add_singer(queue):
    """Add a singer to the queue."""
    name, song = prompt_for_singer()
    queue.append((name, song))
    print(f"Added {name} to the queue.")

def remove_singer(queue):
    """Remove a singer from the queue."""
    name = input("Who do you want to remove? ").strip().title()
    for i, (singer, song) in enumerate(queue, start=1):
        if singer == name:
            queue.pop(i - 1)
            print(f"Removed {name} from the queue.")
            return
    print(f"There's no one named {name} in the queue.")


def show_queue(queue):
    """Show the current queue of singers."""
    print("\n============================================")
    print("Current Queue:")
    print("============================================")
    for i, (singer, song) in enumerate(queue, start=1):
        print(f"{i}. {singer} - {song}")
    print("\nOptions: add / remove / show / next / quit")
    print("> ")

def run_app(queue):
    """Run the karaoke app."""
    while True:
        command = input("Enter a command (add, remove, show, next, quit): ")
        if command == "add":
            add_singer(queue)
        elif command == "remove":
            remove_singer(queue)
        elif command == "show":
            show_queue(queue)
        elif command == "next":
            next_singer(queue)
        elif command == "quit":
            print("Exiting the app.")
            break
        else:
            print(f"Unrecognized command: {command}. Please try again.")

def next_singer(queue):
    if not queue:
        print("The queue is empty.")
        return
    name, song = queue.pop(0)
    print(f"NOW UP: {name} — {song}")

def main():
    queue = [("Annie", "Dancing Queen"), ("Allen", "Country Roads")]
    run_app(queue)  
    
if __name__ == "__main__":
    main()
    
print("App has exited.")