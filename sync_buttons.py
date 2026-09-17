import re
import glob

# The correct buttons block
buttons_html = '''
<!-- Floating Quick WhatsApp / Contact Action -->
<a aria-label="Call JustProtex" class="mobile-call-btn fixed bottom-[90px] lg:bottom-6 left-6 w-14 h-14 bg-brand-charcoal text-white rounded-full shadow-2xl flex items-center justify-center hover:scale-110 transition-transform z-50" style="background-color: #111111;" href="tel:+919802737371">
  <svg class="w-6 h-6" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M2.25 6.75c0 8.284 6.716 15 15 15h2.25a2.25 2.25 0 0 0 2.25-2.25v-1.372c0-.516-.351-.966-.852-1.091l-4.423-1.106c-.44-.11-.902.055-1.173.417l-.97 1.293c-2.896-1.596-5.273-3.973-6.869-6.869l1.293-.97c.362-.271.527-.733.417-1.173L6.963 3.102a1.125 1.125 0 0 0-1.091-.852H4.5A2.25 2.25 0 0 0 2.25 4.5v2.25Z"></path></svg>
</a>

<a aria-label="Chat on WhatsApp" style="background-color: #25D366;" class="fixed bottom-[90px] lg:bottom-6 right-6 w-14 h-14 text-white rounded-full shadow-2xl flex items-center justify-center hover:scale-110 transition-transform z-50 group" href="https://api.whatsapp.com/send/?phone=919802737371" rel="noopener noreferrer" target="_blank">
  <svg class="w-7 h-7" fill="currentColor" viewBox="0 0 24 24"><path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51a12.8 12.8 0 0 0-.57-.01c-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 0 1-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 0 1-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 0 1 2.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0 0 12.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 0 0 5.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 0 0-3.48-8.413Z"/></svg>
</a>
'''

html_files = glob.glob('*.html')
for file in html_files:
    if file in ['header.html', 'head.html', 'footer.html']: continue
    
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Remove existing call button
    content = re.sub(r'<a[^>]*aria-label="Call JustProtex".*?</a>', '', content, flags=re.DOTALL)
    # Remove existing whatsapp button
    content = re.sub(r'<a[^>]*aria-label="Chat on WhatsApp".*?</a>', '', content, flags=re.DOTALL)
    # Remove floating action comment
    content = re.sub(r'<!-- Floating Quick WhatsApp / Contact Action -->', '', content)
    
    # Inject before <script src="js/main.js"> or </body>
    if '<script src="js/main.js">' in content:
        content = content.replace('<script src="js/main.js">', buttons_html + '\n<script src="js/main.js">')
    else:
        content = content.replace('</body>', buttons_html + '\n</body>')
        
    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f'Synced floating buttons in {file}')
