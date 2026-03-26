"""Interactive character command with textual interface."""

from bit.character_frames import IDLE_FRAMES, SLEEPING_FRAMES, WORKING_FRAMES


def display_character(state: str) -> None:
    """Display the character frame for the given state."""
    if state == "idle":
        frame = IDLE_FRAMES[0]
    elif state == "sleeping":
        frame = SLEEPING_FRAMES[0]
    elif state == "working":
        frame = WORKING_FRAMES[0]
    else:
        frame = IDLE_FRAMES[0]

    for line in frame:
        print(line)


def character() -> None:
    """Interactive character - commands: /idle, /sleep, /work, /quit."""
    state = "idle"

    print("Bem-vindo ao character! Digite mensagens ou use /idle, /sleep, /work, /quit")
    print()
    display_character(state)
    print()

    while True:
        try:
            message = input("> ").strip()
        except EOFError:
            break

        if not message:
            continue

        if message.startswith("/"):
            command = message.lower()
            if command == "/idle":
                state = "idle"
                print()
                display_character(state)
                print()
            elif command == "/sleep":
                state = "sleeping"
                print()
                display_character(state)
                print()
            elif command == "/work":
                state = "working"
                print()
                display_character(state)
                print()
            elif command == "/quit":
                break
            else:
                print(f"Comando desconhecido: {command}")
        else:
            # Echo message
            print(f"Você: {message}")


if __name__ == "__main__":
    character()
