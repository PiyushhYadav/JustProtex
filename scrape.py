import urllib.request
import re

url = "https://unsplash.com/s/photos/fingerprint"
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
try:
    html = urllib.request.urlopen(req).read().decode('utf-8')
    matches = set(re.findall(r'(https://images\.unsplash\.com/photo-[a-zA-Z0-9\-]+)', html))
    print("Found IDs:")
    for m in list(matches)[:10]:
        print(m)
except Exception as e:
    print("Error:", e)
