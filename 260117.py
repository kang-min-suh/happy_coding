import retext = "너 스스로 깨닫도록 스스로를 응원하자!  # 12:33  루."

times = re.findall(r'\b\d{2}:\d{2}\b', text)
print(times)

last_time = times[-1] if times else None
print(last_time)