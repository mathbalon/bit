"""ASCII art frames for the character animation loaded from YAML."""

from pathlib import Path

import yaml


def load_frames_from_yaml():
    """Load character frames from frames.yaml."""
    yaml_path = Path(__file__).parent / "frames.yaml"
    with open(yaml_path) as f:
        data = yaml.safe_load(f)

    frames_data = data.get("frames", {})

    # Convert each frame string to a list of lines
    idle = [frame.strip().split("\n") for frame in frames_data.get("idle", [])]
    sleeping = [frame.strip().split("\n") for frame in frames_data.get("sleeping", [])]
    working = [frame.strip().split("\n") for frame in frames_data.get("working", [])]

    return idle, sleeping, working


IDLE_FRAMES, SLEEPING_FRAMES, WORKING_FRAMES = load_frames_from_yaml()
