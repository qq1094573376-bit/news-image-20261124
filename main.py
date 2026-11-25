import base64, os, pathlib, sys
here = pathlib.Path(__file__).resolve().parent
out = pathlib.Path(sys.argv[1]) if len(sys.argv) > 1 else pathlib.Path(os.environ.get("OUTPUT_PATH", "/output/entry.png"))
out.parent.mkdir(parents=True, exist_ok=True)
data = base64.b64decode((here / "entry.png.b64").read_text().strip())
out.write_bytes(data)
