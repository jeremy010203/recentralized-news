import time

class Content:
    receive_time = None
    expire_at = None
    raw_content = None

    def __init__(self, timeout, content):
        self.receive_time = int(time.time())
        self.expire_at = self.receive_time + timeout
        self.raw_content = content

    def is_expired(self):
        return self.expire_at < int(time.time())
