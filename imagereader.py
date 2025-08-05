import os, math

# 1) Figure out where this script lives on disk:
script_dir = os.path.dirname(os.path.abspath(__file__))

# 2) Build the path to the images folder:
images_dir = os.path.join(script_dir, 'images')

# 3) List only .webp files in that folder:
files = sorted(f for f in os.listdir(images_dir) if f.lower().endswith('.webp'))

# Optional sanity check: print how many it found:
print(f"Found {len(files)} .webp files in {images_dir!r}", file=os.sys.stderr)

# 4) Calculate how many per page (100 pages total):
per_page = math.ceil(len(files) / 100)

# 5) Emit HTML snippets, grouped by page:
for page in range(100):
    start = page * per_page
    end   = (page + 1) * per_page
    page_files = files[start:end]
    print(f'<!-- Page {page+1} ({len(page_files)} images) -->')
    for fn in page_files:
        # adjust path in href/src so it matches your repo layout
        print(f'<a href="images/{fn}"><img src="images/{fn}" alt="{fn}"></a>')
    print()
