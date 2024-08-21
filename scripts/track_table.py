import datetime
from rich.table import Table
from rich.layout import Layout


# Creates layout for printing table
def make_layout():
  layout = Layout()
  layout.split(
    Layout(name="header", ratio=1),
    Layout(name="body", ratio=5)
  )
  return layout


# Returns track table
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
    table.add_row(f"{track.id}",f"{track.name}",f"{track.artist_name}", f"{track.popularity}",f"{str(datetime.timedelta(seconds=round(track.duration / 1000)))}",f"{track.explicit}")

  return table