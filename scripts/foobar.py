import time

from rich.table import Table
from rich.live import Live
from rich.layout import Layout
import keyboard

from models.track import Track

tracks = [Track(1, "foo", 10, 50, False, "-"),
          Track(2, "bar", 10, 50, False, "-"),
          Track(3, "quux", 10, 50, False, "-"),
          Track(4, "baz", 10, 50, False, "-")
        ]
table = Table(expand=True)

table.add_column("Track ID",ratio=1)
table.add_column("Name",ratio=6)
table.add_column("Popularity",ratio=1)
table.add_column("Duration",ratio=1)
table.add_column("Explicit",ratio=1)
table.add_column("External URLs",ratio=6)

for track in tracks:
  table.add_row(f"{track.id}",f"{track.name}",f"{track.popularity}",f"{track.duration}",f"{track.explicit}", f"{track.external_URLs}")

def make_layout():
  layout = Layout()
  layout.split(
    Layout(name="header", ratio=1),
    Layout(name="body", ratio=5)
  )
  return layout

layout = make_layout()
layout['body'].update(table)

with Live(layout, refresh_per_second=4) as live:
  while True:
    time.sleep(0.2)
    event = keyboard.read_event()
    if event.event_type == keyboard.KEY_DOWN and event.name == 'q':
      break

    table.add_row(event.name)
