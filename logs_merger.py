import argparse
from pathlib import Path

arg_parser = argparse.ArgumentParser()
arg_parser.add_argument("filenames", nargs="*", help="List of files to merge")
arg_parser.add_argument(
    "--output",
    "-o",
    default="merge_output.txt",
    help="Output file path (If the directory is the same as this file, it will save to the output directory)",
)
args = arg_parser.parse_args()


def get_output_dir(filename: str) -> str:
    if Path(__file__).parent == Path(filename).resolve().parent:
        return f"./output/{filename}"
    else:
        return filename


Path("./output").mkdir(parents=True, exist_ok=True)
output_file = get_output_dir(args.output)

all_lines = []
for file_raw in args.filenames:
    file = get_output_dir(file_raw)
    with open(file, encoding="utf-8") as f:
        all_lines.extend(f.read().split('\n'))
with open(output_file, "w", encoding="utf-8") as f:
    f.write("\n".join(sorted(all_lines)))
