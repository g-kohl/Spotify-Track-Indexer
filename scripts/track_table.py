from rich.table import Table

# TODO: adjust ratios and minimum sizes (for small terminals)
def generate_track_table(tracks, page, page_size):
  table = Table(expand=True)

  table.add_column("Track ID",ratio=1)
  table.add_column("Name",ratio=6)
  table.add_column("Artist",ratio=6)
  table.add_column("Popularity",ratio=1)
  table.add_column("Duration",ratio=1)
  table.add_column("Explicit",ratio=1)

  page_tracks = tracks[(page * page_size):((page + 1) * page_size)]

  for track in page_tracks:
    table.add_row(f"{track.id}",f"{track.name}",f"{track.artist_name}", f"{track.popularity}",f"{track.duration}",f"{track.explicit}")

  return table