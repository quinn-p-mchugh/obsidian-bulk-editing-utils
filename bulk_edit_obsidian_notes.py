"""Function for retrieving files from a specified directory, optionally matching a list of file extensions.
@author Quinn McHugh
@website https://quinnmchugh.net/
"""

from pathlib import Path
from typing import List
from datetime import datetime
import re

PATH = Path(r"C:\Users\Quinn\My Drive\My Vault")
FILE_EXTENSIONS = ["md"]


def get_files(
    dir: Path, exts: List[str] = None, recursive: bool = True
) -> List[Path]:
    """Get a list of files from a specified directory.
    Args:
        path (Path): The directory to search.
        exts (List[str]): A list of file extensions to search for.
        recursive (bool): Whether or not subdirectories should be searched recursively.
    Return:
        List[Path]: A list of files retrieved from the search.
    """
    search_str = "**/*" if recursive else "*"

    file_list = []
    if exts:
        for ext in exts:
            for f in dir.glob(f"{search_str}.{ext}"):
                file_list.append(f)
    else:
        for f in dir.glob(f"{search_str}"):
            file_list.append(f)

    return file_list


files = get_files(dir=PATH, exts=FILE_EXTENSIONS, recursive=True)


def format_tags_and_links(str):
    regex_match_tags = re.compile(r"#[^\s]+")
    regex_match_links = re.compile(r"\[\[[^\[\[\]\]]+\]\]")
    tags = re.findall(regex_match_tags, str)
    links = re.findall(regex_match_links, str)
    return f"""@tags:: {' '.join([tag for tag in tags])}
@links:: {' '.join([link for link in links])}\n"""


def get_date_from_metadata(str):
    arr = str.splitlines()
    date_metadata = ""
    for line in arr:
        if "date:" in line:
            date_metadata = line
            break
    date = date_metadata.split(":")[1].strip()
    return date


for f in files:
    # print(f"Opening {f.name}")
    with open(f, "r", encoding="utf8") as file:
        file_data = file.read()
        m_timestamp = f.stat().st_mtime
        c_timestamp = f.stat().st_ctime
        m_datetime = datetime.fromtimestamp(m_timestamp).astimezone()
        c_datetime = datetime.fromtimestamp(c_timestamp).astimezone()

        # regex = r"(---){1}((?:.|\n)*)(---){1}((?:.|\n)*)(# <%\+ tp\.file\.title %>)"
        regex = r"(---){1}((?:.|\n)*)(---){1}((?:.|\n)*)(> \[!QUOTE\] )"
        if (
            "date:" in file_data
            and not any(x in file_data for x in ["@created::"])
            and re.match(regex, file_data)
        ):
            print(f"Opening {f.name}")
            print(file_data)
            file_data = re.sub(
                regex,  # Match space between bottom bound of metadata and note title
                lambda match: f"{match.group(1)}{match.group(2)}{match.group(3)}\n@created:: [[{get_date_from_metadata(match.group(2))}]]{match.group(4)}{match.group(5)}",
                file_data,
            )
            print(file_data)

        """
        if not any(
            x in file_data for x in ["@tags::", "@links::"]
        ) and re.match(regex, file_data):
            print(f"Opening {f.name}")
            print(file_data)
            file_data = re.sub(
                regex,  # Match space between bottom bound of metadata and note title
                lambda match: f"{match.group(1)}{match.group(2)}{match.group(3)}\n{format_tags_and_links(match.group(4))}{match.group(5)}",
                file_data,
            )
            print(file_data)"""

    if "000 Meta" not in str(f.resolve()):
        """Replace date: and time: in metadata with actual file creation date and time"""

        """c_date = c_datetime.strftime("%Y-%m-%d")
        file_data = re.sub(
                r"(date: )(?:(?:\d{4}-(?:0[1-9]|1[0-2])-(?:0[1-9]|[12][0-9]|3[01]))|{{date}})",
                lambda match: fr"{match.group(1)}{c_date}",
                file_data,
            )

        slice = -2
        c_time = c_datetime.strftime("%H:%M %z")
        c_time_with_time_zone_colon = "{0}:{1}".format(
            c_time[:slice], c_time[slice:]
        )
        file_data = re.sub(
                r"(time: )(?:(?:2[0-3]|[01][0-9]:[0-5][0-9]) (?:[+-](?:2[0-3]|[01][0-9]):[0-5][0-9])|{{time}})",
                lambda match: fr"{match.group(1)}{c_time_with_time_zone_colon}",
                file_data,
            )"""

    """file_data = re.sub(
            r"([*]{1,3}[ A-Za-z0-9$&+,:;=?@#|'<>.^*()%!-]*[*]{0,2})\-",
            lambda match: fr"{match.group(1)}*",
            file_data,
        )"""

    '''file_data = file_data.replace("[[Links]]", "@links: ")
    file_data = file_data.replace(
        """
#status🚦/🔴red #lit✍/📚book""",
        """@tags: #lit✍/📚book #status🚦/🔴red
@links: """,
    )
    file_data = file_data.replace(c
        """
    #status🚦/🔴red #lit✍/🎧️podcast 
[[Links]]""",
        """@tags: #lit✍ #status🚦/🔴red
@links: """,
    )

    """ # How to replace every instance of 4 spaces with a hyphen at the end with a tab (/t)?"""
    file_data = file_data.replace("- ", "- ",)
    file_data = file_data.replace("    - ", "\t- ",)
    file_data = file_data.replace("        - ", "\t\t- ",)
    file_data = file_data.replace("            - ", "\t\t\t- ",)
    file_data = file_data.replace("                - ", "\t\t\t\t- ",)
    file_data = file_data.replace("                    - ", "\t\t\t\t\t- ",)
    file_data = file_data.replace(
        "                        - ", "\t\t\t\t\t\t- ",
    )
    file_data = file_data.replace(
        "                            - ", "\t\t\t\t\t\t\t- ",
    )
    file_data = file_data.replace(
        "                                - ", "\t\t\t\t\t\t\t\t- ",
    )
    file_data = file_data.replace(
        "                                    - ", "\t\t\t\t\t\t\t\t\t- ",
    )
    file_data = file_data.replace("* ", "- ",)
    file_data = file_data.replace("    * ", "\t- ",)
    file_data = file_data.replace("        * ", "\t\t- ",)
    file_data = file_data.replace("            * ", "\t\t\t- ",)
    file_data = file_data.replace("                * ", "\t\t\t\t- ",)
    file_data = file_data.replace("                    * ", "\t\t\t\t\t- ",)
    file_data = file_data.replace(
        "                        * ", "\t\t\t\t\t\t- ",
    )
    file_data = file_data.replace(
        "                            * ", "\t\t\t\t\t\t\t- ",
    )
    file_data = file_data.replace(
        "                                * ", "\t\t\t\t\t\t\t\t- ",
    )
    file_data = file_data.replace(
        "                                    * ", "\t\t\t\t\t\t\t\t\t- ",
    )'''

    with open(f, "w", encoding="utf8") as file:
        file.write(file_data)
