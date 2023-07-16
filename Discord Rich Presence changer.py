from discordrp import Presence
import time

client_id = "0"  # id field

with Presence(client_id) as presence:
    presence.set(
        {
            "state": "5.7 Months elapsed",
            "details": "How do i close the binding of isac?????",
        }
    )

    while True:
        time.sleep(15)