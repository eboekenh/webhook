import requests

TOPIC = "ecem-bildirim-x7k9p4-2026"


def notify(message):
    requests.post(f"https://ntfy.sh/{TOPIC}", data=message.encode("utf-8"))


if __name__ == "__main__":
    notify("Test bildirimi: webhook calisiyor!")
