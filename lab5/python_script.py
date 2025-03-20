# Justin Heinrichs (qtr4sk)

import json
import pandas as pd

with open('schacon.repos.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

data_list = []

for item in data:
    data_list.append({
        "name": item.get("name"),
        "html_url": item.get("html_url"),
        "updated_at": item.get("updated_at"),
        "visibility": item.get("visibility")
    })

df = pd.DataFrame(data_list)

df.head(5).to_csv("chacon.csv", index=False, header=False)
