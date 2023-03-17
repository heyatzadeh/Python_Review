import re

example = "https://google.codm"
urlPattern = r"(https?://)?(www.)?([a-zA-Z0-9]+)\.[\D]{2,3}"
result = re.finditer(urlPattern, example)
for r in result:
    print(r)
