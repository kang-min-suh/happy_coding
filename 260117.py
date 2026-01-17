import re 
text_full = ["나는 행복하다. #23:59 루."]
pattern = r'\b\d{2}:\d{2}\b'
last_times = [
    re.findall(pattern, text)[-1] if re.findall(pattern, text) else None
    for text in text_full
]
print(last_times)