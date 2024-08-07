import time

from rich.live import Live
from rich.layout import Layout
from rich.text import Text
import keyboard
import math

from models.track import Track
from scripts.track_table import generate_track_table

tracks = [Track(1, "foo", 10, 50, False, "foo"),
          Track(2, "bar", 10, 50, False, "foo"),
          Track(3, "quux", 10, 50, False, "foo"),
          Track(4, "baz", 10, 50, False, "foo")
        ]

def make_layout():
  layout = Layout()
  layout.split(
    Layout(name="header", ratio=1),
    Layout(name="body", ratio=5)
  )
  return layout


page_size = 3
current_page = 0
total_pages = math.ceil(len(tracks) / page_size)

layout = make_layout()
layout['body'].update(generate_track_table(tracks, current_page, page_size))

with Live(layout) as live:

  while True:
    time.sleep(0.2)
    event = keyboard.read_event()

    if event.event_type == keyboard.KEY_DOWN:
      layout['header'].update(Text(event.name, justify="center"))

    if event.event_type == keyboard.KEY_DOWN and event.name == "right" or event.name == "down":
      current_page = current_page + 1 if current_page + 1 < total_pages else current_page  
      layout['body'].update(generate_track_table(tracks, current_page, page_size))

    if event.event_type == keyboard.KEY_DOWN and event.name == "left" or event.name == "up":
      current_page = current_page - 1 if current_page > 0 else current_page  
      layout['body'].update(generate_track_table(tracks, current_page, page_size))

    if event.event_type == keyboard.KEY_DOWN and event.name == 'q':
      break