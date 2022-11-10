import pandas as pd
from pathlib import Path
import numpy as np
from time import sleep

quotes = pd.read_csv(Path(__file__).parent / "Quotes.csv")

for index, row in quotes.iterrows():
    print(row)
    favorite = "true" if row["Favorite?"] == "Yes" else ""
    tags = row["Tags"]
    tags = " ".join(
        ""
        if type(tags) != str
        else [
            f'[[{tag.replace("-", " ").strip().title()}]]'
            for tag in tags.split(", ")
        ]
    )

    comments = (
        "" if type(row["Comments"]) != str else "\n" + row["Comments"] + "\n"
    )

    file_data = f"""---
date: {row["Created"]}
time: {row["Time"]}
aliases: 
favorite: {favorite}
---
@tags: #perm📝/quote💬
@links: {tags}
@attributed-to: [[{"" if type(row["Author"]) != str else row["Author"]}]]
> [!QUOTE] 
> {row["Quote"]}
{comments}
---
## Related
- 

## References
- """

    # print(file_data)'
    file_name = (
        str(row["Quote"])
        .replace("“", "")
        .replace("”", "")
        .replace("\n", " ")
        .replace('"', "")
        .replace("?", ".")[:252]
        + r".md"
    )
    file_path = Path(
        r"C:/Users/Quinn/Documents/Code Repositories/obsidian-bulk-editing-utils/generated_quotes/"
        + file_name
    )
    with open(file_path, "w", encoding="utf8") as f:
        f.write(file_data)
        sleep(2)

