import os
import glob
import re

html_files = glob.glob('*.html')

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Use regex to find and remove the script tag containing tailwind.config
    new_content = re.sub(r'<script>\s*tailwind\.config\s*=\s*\{.*?</script>', '', content, flags=re.DOTALL)
    
    if new_content != content:
        with open(file, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f'Removed tailwind.config script from {file}')

