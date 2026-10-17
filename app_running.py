queue = [("Annie", "Dancing Queen"), ("Allen", "Country Roads")]

# prompt for singer

def prompt_for_singer():
    if len(queue) < 2:
        print("You need at least two singers in the queue to move someone to the top.")
        return "", ""
    """Prompt the host for a singer's name and song."""
    name = input("Enter the singer's name: ").strip().title()
    song = input("Enter the song: ").strip().title()
    return name, song

def add_singer(queue):
    name, song = prompt_for_singer()
    if name == "" or song == "":
        print("Oops! I need a name and a song to add someone to the queue.")
        return
    
    """Add a singer to the queue."""
    name, song = prompt_for_singer()
    queue.append((name, song))
    print(f"Added {name} to the queue.")

def remove_singer(queue):
    if len(queue) == 0:
        print("Oops! There's no one left to call up!")
        return

    """Remove a singer from the queue."""
    name = input("Who do you want to remove? ").strip().title()
    for i, (singer, song) in enumerate(queue, start=1):
        if singer == name:
            queue.pop(i - 1)
            print(f"Removed {name} from the queue.")
            return
    print(f"There's no one named {name} in the queue.")

def move_to_top(queue):
    if len(queue) == 0:
        print("Oops! There's no one left to move!")
        return
    if queue[0] == queue[-1]:
        print("There's only one singer in the queue. No need to move anyone.")
        return
    
    """Move a singer to the top of the queue."""
    position = int(input("Who do you want to move to the top? Enter a number: ")) - 1
    if 0 <= position < len(queue):
        singer, song = queue.pop(position)
        queue.insert(0, (singer, song))
        print(f"Moved {singer} to the top of the queue!")
    else:
        print("Invalid position.")

def show_queue(queue):
    if len(queue) == 0:
        print("Oops! There's no one left to show!")
        return
    
    """Show the current queue of singers."""
    print("\n============================================")
    print("Current Queue:")
    print("============================================")
    for i, (singer, song) in enumerate(queue, start=1):
        print(f"{i}. {singer} - {song}")
    print("\nOptions: add / remove / show / next / top / quit")
    print("> ")

def run_app(queue):
    """Run the karaoke app."""
    while True:
        command = input("Enter a command (add, remove, show, next, top, quit): ")
        if command == "add":
            add_singer(queue)
        elif command == "remove":
            remove_singer(queue)
        elif command == "show":
            show_queue(queue)
        elif command == "next":
            next_singer(queue)
        elif command == "top":
            move_to_top(queue)
        elif command == "quit":
            print("Exiting the app.")
            break
        else:
            print(f"Unrecognized command: {command}. Please try again.")

def next_singer(queue):
    if len(queue) == 0:
        print("Oops! There's no one left to call up!")
        return
    
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