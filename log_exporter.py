import argparse
from pathlib import Path
import requests
import time


arg_parser = argparse.ArgumentParser()
arg_parser.add_argument("--username", "-U", help="Username to search for")
arg_parser.add_argument("--text", "-T", help="Text to search for")
arg_parser.add_argument(
    "--channel", "-C", default="Destinygg", help="Channel to search in"
)
arg_parser.add_argument(
    "--start", "-S", help="Start date of search in YYYY-MM-DD format"
)
arg_parser.add_argument("--end", "-E", help="End date of search in YYYY-MM-DD format")
arg_parser.add_argument(
    "--searchafter", type=int, help="End date of search in YYYY-MM-DD format"
)
arg_parser.add_argument(
    "--output",
    "-o",
    default="output.txt",
    help="Filepath to save logs at. (If the directory is the same as this file, it will save to the output directory)",
)
arg_parser.add_argument(
    "--max_pages",
    "-p",
    type=int,
    default=-1,
    help="Number of pages/requests to make while paginating",
)
args = arg_parser.parse_args()

Path("./output").mkdir(parents=True, exist_ok=True)
if Path(__file__).parent == Path(args.output).resolve().parent:
    output_file = f"./output/{args.output}"
else:
    output_file = args.output

url = "https://api-v2.rustlesearch.dev/anon/search"
payload = {
    "username": args.username,
    "text": args.text,
    "start_date": args.start,
    "end_date": args.end,
    "channel": args.channel,
    "search_after": args.searchafter,
}

# paginate
page = args.max_pages
search_after = None
messages = []
while (
    page
):  # until page reaches 0 (if max_pages is -1, then continue until no more messages are returned)
    payload["search_after"] = search_after
    r = requests.get(url, params=payload)
    print(r.url)
    new_messages = r.json()["data"]["messages"]
    if not len(new_messages):
        break
    messages.extend(new_messages)
    search_after = new_messages[-1]["searchAfter"]
    page -= 1
    time.sleep(1)

text = "\n".join(
    f"[{message['ts']}] {message['username']}: {message['text']}"
    for message in reversed(messages)
)
with open(output_file, "w", encoding="utf-8") as f:
    f.write(text)
