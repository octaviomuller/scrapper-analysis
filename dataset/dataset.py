import os
import pandas as pd
from typing import Any

class Dataset:
    def __init__(self, path: str, data: dict[str, Any]):
        self.path = path
        self.data = data

    def save(self):
        df = None

        if os.path.getsize(self.path) == 0:
            df = pd.DataFrame({}, columns=self.data.keys())
        else:
            df = pd.read_csv(self.path)

        if self.data['url'] in df['url'].values:
            df.loc[df['url'] == self.data['url']] = self.data
        else:
            df = pd.concat([df, pd.DataFrame([self.data])], ignore_index=True)

        df.to_csv(self.path, index=False)
