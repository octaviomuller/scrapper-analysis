import csv
from typing import Any

class Dataset:
    def __init__(self, path: str, data: dict[str, Any]):
        self.path = path
        self.data = data

    def save(self):
        header = list(self.data.keys())
        values = list(self.data.values())

        try:
            with open(self.path, 'r', newline='') as f:
                reader = csv.DictReader(f)
                lines = list(reader)

                url_found = False
                for i, line in enumerate(lines):
                    if line["url"] == self.data.get("url", ""):
                        lines[i] = self.data
                        url_found = True
                        break
        except FileNotFoundError:
            lines = []
            url_found = False

        if not url_found:
            lines.append(self.data)

        with open(self.path, 'w', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=header)
            if not url_found:
                writer.writeheader()
            writer.writerows(lines)
