import csv
from typing import Any

class Dataset:
    def __init__(self, path: str, data: dict[str, Any]):
        self.path = path
        self.data = data

    def save(self):
        lines = []
        url_found = False
        values = [str(v) for v in self.data.values()]

        try:
            with open(self.path, 'r', newline='') as f:
                reader = csv.reader(f)
                l = list(reader)

                for i, line in enumerate(l):
                    if line and line[-1] == self.data["url"]:
                        lines[i] = values
                        url_found = True
                        break
        except FileNotFoundError:
            with open(self.path, 'w', newline='') as f:
                pass

        if not url_found:
            lines.append(values)

        with open(self.path, 'w', newline='') as f:
            reader = csv.writer(f)
            reader.writerows(lines)