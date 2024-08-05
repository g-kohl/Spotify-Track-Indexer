import time

from rich.live import Live
from rich.layout import Layout
import keyboard

from models.track import Track
from track_table import generate_track_table

tracks = [Track(1, "foo", 10, 50, False, "-"),
          Track(2, "bar", 10, 50, False, "-"),
          Track(3, "quux", 10, 50, False, "-"),
          Track(4, "baz", 10, 50, False, "-")
        ]

def make_layout():
  layout = Layout()
  layout.split(
    Layout(name="header", ratio=1),
    Layout(name="body", ratio=5)
  )
  return layout

layout = make_layout()
layout['body'].update(generate_track_table(tracks))

with Live(layout, refresh_per_second=4) as live:
  while True:
    time.sleep(0.2)
    event = keyboard.read_event()
    if event.event_type == keyboard.KEY_DOWN and event.name == 'q':
      break