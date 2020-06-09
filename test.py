import time

from infinity import Infinity
from infinity import User

u = User()
i = Infinity("wlp2s0")
i.set_wifi_state(enabled=False)
i.randomize_mac()
i.set_wifi_state(enabled=True)
time.sleep(8)
i.handle_portal(u)
