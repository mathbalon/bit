"""Interactive character command with textual interface."""

from textual.app import App, ComposeResult, RenderableType
from textual.binding import Binding
from textual.widgets import Input, Static

from bit.character_frames import IDLE_FRAMES, SLEEPING_FRAMES, WORKING_FRAMES


class CharacterDisplay(Static):
    """Display character animation with loop-independent rendering."""

    def __init__(self):
        super().__init__()
        self.state = "idle"
        self.frame_index = 0
        self.all_frames = {
            "idle": IDLE_FRAMES,
            "sleeping": SLEEPING_FRAMES,
            "working": WORKING_FRAMES,
        }

    def render(self) -> RenderableType:
        """Render current frame aligned to bottom-left."""
        frames = self.all_frames.get(self.state, IDLE_FRAMES)
        if not frames:
            return ""

        frame = frames[self.frame_index % len(frames)]
        frame_lines = list(frame)

        # Get widget size
        width = self.size.width if self.size else 0
        height = self.size.height if self.size else 0

        if width <= 0 or height <= 0:
            return "\n".join(frame_lines)

        # Pad frame lines to full width and collect all lines
        padded_lines = []
        for line in frame_lines:
            # Ensure line is not longer than widget width
            line = line[:width] if len(line) > width else line
            padded_lines.append(line)

        # Calculate padding needed for bottom alignment
        frame_height = len(padded_lines)
        top_padding = max(0, height - frame_height)

        # Build final output: empty lines on top + frame at bottom
        result_lines = ["" for _ in range(top_padding)] + padded_lines
        return "\n".join(result_lines)

    def advance_frame(self) -> None:
        """Advance to next frame."""
        frames = self.all_frames.get(self.state, IDLE_FRAMES)
        if frames:
            self.frame_index += 1
        self.refresh()

    def set_state(self, new_state: str) -> None:
        """Change character state."""
        if new_state in self.all_frames:
            self.state = new_state
            self.frame_index = 0
        self.refresh()


class MessageDisplay(Static):
    """Show only the latest user message."""

    def __init__(self):
        super().__init__("Bem-vindo! Digite algo ou use /idle, /sleep, /work")

    def update_message(self, message: str) -> None:
        """Update the displayed message."""
        self.update(message)


class CharacterApp(App):
    """Main character app."""

    BINDINGS = [
        Binding("ctrl+c", "quit", "Sair"),
    ]

    CSS = """
    Screen {
        layout: vertical;
    }

    CharacterDisplay {
        border: solid $primary;
        width: 1fr;
        height: 1fr;
    }

    MessageDisplay {
        border: solid $secondary;
        width: 1fr;
        height: 3;
    }

    Input {
        margin: 1;
        border: solid $accent;
    }
    """

    def compose(self) -> ComposeResult:
        """Compose app layout."""
        yield CharacterDisplay()
        yield MessageDisplay()
        yield Input(id="char_input")

    def on_mount(self) -> None:
        """Start animation timer when app mounts."""
        self.set_interval(0.3, self._animate_character)
        input_widget = self.query_one(Input)
        input_widget.focus()

    def _animate_character(self) -> None:
        """Advance character animation frame."""
        char_display = self.query_one(CharacterDisplay)
        char_display.advance_frame()

    def on_input_submitted(self, event: Input.Submitted) -> None:
        """Handle input submission."""
        message = event.value.strip()
        event.control.value = ""  # Clear input

        if not message:
            return

        if message.startswith("/"):
            self._handle_command(message)
        else:
            # Display user message
            msg_display = self.query_one(MessageDisplay)
            msg_display.update_message(f"Você: {message}")

    def _handle_command(self, command: str) -> None:
        """Handle commands."""
        char_display = self.query_one(CharacterDisplay)
        msg_display = self.query_one(MessageDisplay)
        cmd = command.lower()

        if cmd == "/idle":
            char_display.set_state("idle")
            msg_display.update_message("✓ Estado: idle")
        elif cmd == "/sleep":
            char_display.set_state("sleeping")
            msg_display.update_message("✓ Estado: sleeping")
        elif cmd == "/work":
            char_display.set_state("working")
            msg_display.update_message("✓ Estado: working")
        elif cmd == "/quit":
            self.exit()
        else:
            msg_display.update_message(f"❌ Comando desconhecido: {command}")


def character() -> None:
    """Run interactive character animation app."""
    app = CharacterApp()
    app.run()


if __name__ == "__main__":
    character()
