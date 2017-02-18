from collections import deque
from time import time


class ClickController(object):
    storage = None
    is_recording = None
    mode = None
    start_time = None
    expno = None
    no_clicking_timeout = None
    last_clicks = None

    def __init__(self, storage, is_recording, mode, expno, no_clicking_timeout):
        self.last_clicks = deque()
        self.storage = storage
        self.is_recording = is_recording
        self.mode = mode
        self.last_clicks.append(0)
        self.expno = expno
        self.no_clicking_timeout = no_clicking_timeout

    def start(self):
        self.start_time = time()

    def on_click(self):
        click_time = time()
        delta = click_time - self.start_time
        self.last_clicks.append(delta)
        if len(self.last_clicks) > 4:
            self.last_clicks.popleft()
        if self.is_recording:
            self.storage.save_experiment_click(time=delta, expno=self.expno)

    def is_not_clicking(self):
        check_delta = time() - self.start_time
        return (check_delta - self.last_clicks[-1]) > self.no_clicking_timeout

    def is_clicking_rhythmically(self):
        if self.mode != 'FEEDBACK_EXPERIMENT':
            return False
        if len(self.last_clicks) < 4:
            return False

        diffs = [(self.last_clicks[i + 1] - self.last_clicks[i]) * 1000 for i in
                 range(0, len(self.last_clicks) - 1)]

        avg = sum(diffs) / len(diffs)
        Q = sum([(d - avg) ** 2 for d in diffs])

        return Q < 10000


class DummyClickController(object):
    def on_click(self):
        pass

    def is_not_clicking(self):
        return False

    def is_clicking_rhythmically(self):
        return False
