import os

def generate_image_html_snippets(folder_path):
    """
    Scan the given folder for image files and generate HTML snippets
    for use in your gallery. All image tags will use relative paths.
    """
    html_snippets = []
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.lower().endswith(('.jpg', '.jpeg', '.png', '.gif', '.bmp', '.webp')):
                # Get relative path for the image
                relative_path = os.path.relpath(os.path.join(root, file), folder_path)
                # Convert backslashes (Windows) to slashes for HTML compatibility
                relative_path = relative_path.replace('\\', '/')
                # Alt text from filename, formatted
                alt_text = os.path.splitext(file)[0].replace('_', ' ').replace('-', ' ').capitalize()
                # Build gallery div
                snippet = (
                    f'<div class="gallery-item">\n'
                    f'  <img class="gallery-img" src="{relative_path}" alt="{alt_text}">\n'
                    f'  <div class="caption">{alt_text}</div>\n'
                    f'</div>'
                )
                html_snippets.append(snippet)
    return html_snippets

# Example usage for folder named "images"
generated_snippets = generate_image_html_snippets('images')
for snippet in generated_snippets:
    print(snippet)
