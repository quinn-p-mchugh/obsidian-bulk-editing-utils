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

for f in files:
    print(f"Opening {f.name}")
    with open(f, "r", encoding="utf8") as file:
        file_data = file.read()
        m_timestamp = f.stat().st_mtime
        c_timestamp = f.stat().st_ctime
        m_datetime = datetime.fromtimestamp(m_timestamp).astimezone()
        c_datetime = datetime.fromtimestamp(c_timestamp).astimezone()

        file_data = file_data.replace("dv.view(", "await dv.view(")

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
