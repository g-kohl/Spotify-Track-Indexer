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
    load_prefix_tree,
    get_track,
    generate_analytics
)

from scripts.track_table import (
    generate_track_table,
    make_layout
)

should_close = False

while not should_close:
    rich.print(Text("Available query options:"))
    rich.print(Text("0 -> Order by popularity"))
    rich.print(Text("1 -> Search by name"))
    rich.print(Text("2 -> Search by prefix"))
    rich.print(Text("3 -> Generate analytics"))
    option = Prompt.ask("Choose an option", choices=["0", "1", "2", "3"])

    build_data_structures()

    popularity_table = load_popularity_table()
    name_tree = load_name_tree()
    prefix_tree = load_prefix_tree()

    if option == "0":
        is_descending = Prompt.ask("Descending order?", choices=["y", "n"], )
        tracks = get_tracks_order_by_popularity(100, is_descending == "y", popularity_table)

    elif option == "1":
        with open("tracks_file.bin", "rb") as track_db:
            tracks = list()

            while len(tracks) == 0:
                name = Prompt.ask("Enter track name")

                try:
                    tracks = [get_track(name_tree.search_key(name), track_db)]
                except:
                    rich.print(Text("Track not found"))
                
            track_db.close()

    elif option == "2":
        with open("tracks_file.bin", "rb") as track_db:
            tracks = list()

            while len(tracks) == 0:
                prefix = Prompt.ask("Enter prefix")
                pointers = prefix_tree.starts_with(prefix.lower())

                if len(pointers) != 0:
                    for p in pointers:
                        tracks.append(get_track(p, track_db))
                else:
                    rich.print(Text("Prefix not found"))

            track_db.close()

        rich.print(Text("Available sorting options:"))
        rich.print(Text("0 -> Order by popularity"))
        rich.print(Text("1 -> Order by track name"))
        rich.print(Text("2 -> Order by artist name"))
        sorting_option = Prompt.ask("Choose an option", choices=["0", "1", "2"])

        sort_track_list(tracks, sorting_option, 0, len(tracks)-1)

    elif option == "3":
        stats = generate_analytics()

        print("Total tracks:", stats['total_tracks'])
        print("Popularity average:", stats['popularity_average'])
        print("Duration average:", stats['duration_average'])
        print("Explicit percentage:", stats['explicit_percentage'])

        should_close = Prompt.ask("Search again?", choices=["y", "n"]) != "y"
        
        if should_close:
            break
        continue

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

            if event.event_type == keyboard.KEY_DOWN and event.name == 'r':
                current_page = 0
                tracks.reverse()
                layout['body'].update(generate_track_table(tracks, current_page, page_size))
                layout['header'].update(Text("Page {}/{}".format(current_page + 1, total_pages), justify="center"))

            if event.event_type == keyboard.KEY_DOWN and event.name == 'q':
                break


    should_close = Prompt.ask("Search again?", choices=["y", "n"]) != "y"
    
    if should_close:
        break