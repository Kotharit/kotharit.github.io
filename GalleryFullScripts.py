import os

# Path to your images folder
folder_path = "images"

# Output HTML file
output_file = "gallery.html"

# Generate gallery items
gallery_items = ""
for filename in sorted(os.listdir(folder_path)):
    if filename.lower().endswith(".webp"):
        src = os.path.join(folder_path, filename).replace("\\", "/")
        caption = os.path.splitext(filename)[0].replace("_", " ")
        item_html = f'''    <div class="gallery-item">
      <div class="image-wrapper">
        <img class="gallery-img" src="{src}" alt="{caption}" loading="lazy">
      </div>
      <div class="caption">{caption}</div>
    </div>\n'''
        gallery_items += item_html

# Full HTML template
html_template = f'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>My Image Gallery</title>
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <style>
    :root {{
      color-scheme: light dark;
    }}
    body {{
      font-family: 'Segoe UI', Arial, sans-serif;
      margin: 0;
      background: #f8fafc;
      color: #222;
      transition: background 0.3s, color 0.3s;
    }}
    h1 {{
      text-align: center;
      font-size: 2.5rem;
      margin: 30px 0 15px;
    }}
    .gallery-container {{
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
      gap: 24px;
      max-width: 1200px;
      margin: auto;
      padding: 24px;
    }}
    .gallery-item {{
      display: flex;
      flex-direction: column;
      border-radius: 10px;
      overflow: hidden;
      box-shadow: 0 2px 8px rgba(50, 50, 93, 0.08);
      background: #fff;
      transition: box-shadow 0.2s, transform 0.2s;
    }}
    .gallery-item:hover {{
      box-shadow: 0 8px 24px rgba(80, 50, 93, 0.16);
      transform: translateY(-3px) scale(1.03);
    }}
    .image-wrapper {{
      aspect-ratio: 16 / 9;
      width: 100%;
      background-color: #ddd;
      overflow: hidden;
      display: flex;
      align-items: center;
      justify-content: center;
    }}
    .gallery-img {{
      width: 100%;
      height: 100%;
      object-fit: cover;
      display: block;
      transition: transform 0.3s ease, opacity 0.3s ease;
    }}
    .gallery-img:hover {{
      transform: scale(1.05);
      opacity: 0.95;
    }}
    .caption {{
      padding: 12px 14px;
      text-align: center;
      font-size: 1rem;
      color: #5a5a5a;
      background-color: #fff;
      border-top: 1px solid #eee;
    }}
    @media (max-width: 600px) {{
      h1 {{
        font-size: 1.8rem;
      }}
      .caption {{
        font-size: 0.95rem;
        padding: 9px 7px;
      }}
    }}
  </style>
</head>
<body>
  <h1>My Image Gallery</h1>
  <div class="gallery-container">
{gallery_items.strip()}
  </div>
</body>
</html>'''

# Write to file
with open(output_file, "w", encoding="utf-8") as f:
    f.write(html_template)

print(f"✅ Gallery generated and saved to {output_file}")
