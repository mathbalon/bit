"""Interactive character command using curses."""

import curses
import time
import typer

from bit.character_frames import IDLE_FRAMES, SLEEPING_FRAMES, WORKING_FRAMES


def draw_frame(stdscr, frame_lines, x_offset, y_offset, color_pair):
    """Draw a frame of the character at the given position."""
    for i, line in enumerate(frame_lines):
        try:
            stdscr.addstr(y_offset + i, x_offset, line, curses.color_pair(color_pair))
        except curses.error:
            pass


def draw_hud(stdscr, state_name, max_y):
    """Draw HUD with current state and controls."""
    try:
        state_display = f"Estado: {state_name}"
        stdscr.addstr(max_y - 3, 3, state_display, curses.color_pair(4))
        stdscr.addstr(
            max_y - 2,
            3,
            "[A] Idle · [S] Sleeping · [D] Working · [Q] Sair",
            curses.color_pair(5),
        )
    except curses.error:
        pass


def animate_state(stdscr, frames, x, y, color, speed=0.2):
    """Play a sequence of frames as animation."""
    for frame in frames:
        stdscr.clear()
        draw_frame(stdscr, frame, x, y, color)
        max_y, _ = stdscr.getmaxyx()
        draw_hud(stdscr, animate_state.current_state, max_y)
        stdscr.refresh()
        time.sleep(speed)


# Global state for HUD
animate_state.current_state = "idle"


def main_loop(stdscr):
    """Main curses loop for character interaction."""
    # Setup curses
    curses.curs_set(0)  # Hide cursor
    stdscr.nodelay(True)  # Non-blocking input
    stdscr.timeout(200)  # Refresh every 200ms

    # Colors
    curses.start_color()
    curses.use_default_colors()
    curses.init_pair(1, curses.COLOR_RED, -1)
    curses.init_pair(2, curses.COLOR_YELLOW, -1)
    curses.init_pair(3, curses.COLOR_GREEN, -1)
    curses.init_pair(4, curses.COLOR_CYAN, -1)
    curses.init_pair(5, curses.COLOR_WHITE, -1)

    # State
    x_pos = 5
    state = "idle"
    frame_index = 0

    animate_state.current_state = "idle"

    while True:
        max_y, max_x = stdscr.getmaxyx()
        y_pos = max(1, (max_y // 2) - 5)

        # Input
        try:
            key = stdscr.getch()
        except:
            key = -1

        # Handle input
        if key == ord("q") or key == ord("Q"):
            break

        elif key == ord("a") or key == ord("A"):
            state = "idle"
            animate_state.current_state = "idle"
            frame_index = 0

        elif key == ord("s") or key == ord("S"):
            state = "sleeping"
            animate_state.current_state = "sleeping"
            frame_index = 0

        elif key == ord("d") or key == ord("D"):
            state = "working"
            animate_state.current_state = "working"
            frame_index = 0

        # Draw based on current state
        stdscr.clear()

        if state == "idle":
            frame = IDLE_FRAMES[frame_index % len(IDLE_FRAMES)]
        elif state == "sleeping":
            frame = SLEEPING_FRAMES[frame_index % len(SLEEPING_FRAMES)]
        elif state == "working":
            frame = WORKING_FRAMES[frame_index % len(WORKING_FRAMES)]
        else:
            frame = IDLE_FRAMES[0]

        draw_frame(stdscr, frame, x_pos, y_pos, 3)
        draw_hud(stdscr, state, max_y)
        stdscr.refresh()

        frame_index += 1
        time.sleep(0.15)


def character() -> None:
    """Interactive character animation. Controls: A (idle) S (sleep) D (work) Q (quit)."""
    curses.wrapper(main_loop)


if __name__ == "__main__":
    character()
