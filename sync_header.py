import re

with open('index.html', 'r', encoding='utf-8') as f:
    index_content = f.read()

header_match = re.search(r'(<!-- BEGIN: TopNotificationBar -->.*?<!-- END: FloatingHeader -->)', index_content, re.DOTALL)
if header_match:
    header_block = header_match.group(1)
    
    with open('header.html', 'r', encoding='utf-8') as f:
        header_file_content = f.read()
    
    # replace the entire content of header.html, assuming it only contains the header
    # wait, let's just replace from TopNotificationBar to FloatingHeader in header.html
    new_header_file = re.sub(r'<!-- BEGIN: TopNotificationBar -->.*?<!-- END: FloatingHeader -->', header_block, header_file_content, flags=re.DOTALL)
    
    with open('header.html', 'w', encoding='utf-8') as f:
        f.write(new_header_file)
    print('Updated header.html')
