import re

html_contact = '''    <div class="mt-4 pt-4 border-t border-brand-border px-6 pb-6">
      <div class="text-xs uppercase font-mono font-bold tracking-widest text-brand-blue mb-3">Direct Contact</div>
      <a href="tel:+919802737371" class="flex items-center gap-3 text-brand-charcoal font-bold text-lg mb-3">
        <svg class="w-5 h-5 text-brand-blue" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" viewBox="0 0 24 24"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"></path></svg>
        +91 98027 37371
      </a>
      <a href="mailto:sales@justprotex.com" class="flex items-center gap-3 text-brand-charcoal font-medium text-sm">
        <svg class="w-5 h-5 text-brand-blue" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" viewBox="0 0 24 24"><path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"></path><polyline points="22,6 12,13 2,6"></polyline></svg>
        sales@justprotex.com
      </a>
    </div>
  </div>
</div>
</header>'''

def insert_mobile_contact(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if "Direct Contact" not in content or "tel:+919802737371" not in content[content.find('mobile-nav-panel'):]:
        new_content = re.sub(r'  </div>\s*</div>\s*</header>', html_contact, content)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)

insert_mobile_contact('index.html')
insert_mobile_contact('about.html')
