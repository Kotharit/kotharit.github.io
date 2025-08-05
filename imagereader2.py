import os

# Path to the images folder
folder_path = "images"

# Output HTML
html_output = ""

# Loop through all files in the folder
for filename in os.listdir(folder_path):
    if filename.lower().endswith(".webp"):
        # Create relative path
        src = os.path.join(folder_path, filename).replace("\\", "/")

        # Create caption by removing extension and replacing underscores
        caption = os.path.splitext(filename)[0].replace("_", " ")

        # Generate HTML block
        html_block = f'''<div class="gallery-item">
  <img class="gallery-img" src="{src}" alt="{caption}">
  <div class="caption">{caption}</div>
</div>
'''
        html_output += html_block

# Print the final HTML
print(html_output)
