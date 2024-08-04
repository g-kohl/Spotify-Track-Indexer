from rich.table import Table

# TODO: adjust ratios and minimum sizes (for small terminals)
# Maybe limit the amount of tracks?
def generate_track_table(tracks):
  table = Table(expand=True)

  table.add_column("Track ID",ratio=1)
  table.add_column("Name",ratio=6)
  table.add_column("Popularity",ratio=1)
  table.add_column("Duration",ratio=1)
  table.add_column("Explicit",ratio=1)
  table.add_column("External URLs",ratio=6)

  for track in tracks:
    table.add_row(f"{track.id}",f"{track.name}",f"{track.popularity}",f"{track.duration}",f"{track.explicit}", f"{track.external_URLs}")

  return table