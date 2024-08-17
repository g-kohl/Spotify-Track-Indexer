import math
import time
from classification_and_pesquisation import *
from rich.live import Live
from rich.text import Text
import keyboard

from data_loader import (
    load_popularity_table, 
    get_most_popular_tracks, 
    build_data_structures
)
from scripts.track_table import (
    generate_track_table,
    make_layout
)


popularity_table = load_popularity_table()

page_size = 10
current_page = 0
total_pages = math.ceil(len(tracks) / page_size)

tracks = get_most_popular_tracks(100, popularity_table)

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