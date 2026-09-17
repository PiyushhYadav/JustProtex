import glob
import re

html_files = glob.glob('*.html')
for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # bump components.js
    content = re.sub(r"src='js/components\.js(\?v=\d+)?'", f"src='js/components.js?v={int(1789668044)}'", content)
    content = re.sub(r'src="js/components\.js(\?v=\d+)?"', f'src="js/components.js?v={int(1789668044)}"', content)
    
    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)
