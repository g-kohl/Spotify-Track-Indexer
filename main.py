import math
import time
from classification_and_pesquisation import *
from rich.live import Live
from rich.text import Text
from rich.prompt import Prompt
import rich
import keyboard

from data_loader import (
    load_popularity_table, 
    get_tracks_order_by_popularity, 
    build_data_structures,
    load_name_tree,
    get_track
)

from scripts.track_table import (
    generate_track_table,
    make_layout
)


rich.print(Text("Available query options:"))
rich.print(Text("0 -> Order by popularity"))
rich.print(Text("1 -> Search by name"))
option = Prompt.ask("Which one?", choices=["0", "1"])

build_data_structures()

popularity_table = load_popularity_table()
name_tree = load_name_tree()

if option == "0":
    is_descending = Prompt.ask("Descending order?", choices=["y", "n"], )
    tracks = get_tracks_order_by_popularity(100, is_descending == "y", popularity_table)

elif option == "1":
    with open("tracks_file.bin", "rb") as track_db:
        name = Prompt.ask("Enter track name")
        tracks = [get_track(name_tree.search_key(name), track_db)]

        track_db.close()

page_size = 10
current_page = 0
total_pages = math.ceil(len(tracks) / page_size)

layout = make_layout()
layout['body'].update(generate_track_table(tracks, current_page, page_size))
layout['header'].update(Text("Page {}/{}".format(current_page + 1, total_pages), justify="center"))

with Live(layout) as live:

  while True:
    time.sleep(0.2)
    event = keyboard.read_event()

    if event.event_type == keyboard.KEY_DOWN and event.name == "right" or event.name == "down":
      current_page = current_page + 1 if current_page + 1 < total_pages else current_page  
      layout['body'].update(generate_track_table(tracks, current_page, page_size))
      layout['header'].update(Text("Page {}/{}".format(current_page + 1, total_pages), justify="center"))

    if event.event_type == keyboard.KEY_DOWN and event.name == "left" or event.name == "up":
      current_page = current_page - 1 if current_page > 0 else current_page  
      layout['body'].update(generate_track_table(tracks, current_page, page_size))
      layout['header'].update(Text("Page {}/{}".format(current_page + 1, total_pages), justify="center"))

    if event.event_type == keyboard.KEY_DOWN and event.name == 'q':
      break