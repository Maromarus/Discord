def read_link():
    try:
        with open("data/link.txt", "r", encoding="utf-8") as f:
            return f.read().strip()
    except FileNotFoundError:
        return "https://example.com"

def write_link(new_link):
    with open("data/link.txt", "w", encoding="utf-8") as f:
        f.write(new_link.strip())