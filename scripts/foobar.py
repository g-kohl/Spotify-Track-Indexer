import time

from rich.table import Table
from rich.live import Live

file = open("./scripts/out.txt", "r", encoding="utf8")
file.readline()

info = list()
for _ in range(500):
  info.append(file.readline().split("-"))

table = Table(title="My tracks")
table.add_column("Playlist name", style="cyan", no_wrap=True)
table.add_column("Track name", style="green", no_wrap=True)

for i in info:
  table.add_row(i[0], i[1])

console = Console()

console.print(table)