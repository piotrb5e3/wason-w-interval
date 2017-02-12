from tinydb import TinyDB

MEASURING_SESSION = 0


class Storage(object):
    db = None
    experiment_data = None
    user_data = None
    clicks = None

    def __init__(self, filename):
        self.db = TinyDB(filename)
        self.experiment_data = self.db.table('exp_data')
        self.user_data = self.db.table('user_data')
        self.clicks = self.db.table('clicks')

    def has_data(self):
        return len(self.user_data) > 0

    def purge(self):
        self.db.purge_table('exp_data')
        self.db.purge_table('user_data')
        self.db.purge_table('clicks')

    def save_benchmark_click(self, time):
        self.clicks.insert({'expno': MEASURING_SESSION, 'time': time})

    def save_experiment_click(self, time, expno):
        self.clicks.insert({'expno': expno, 'time': time})

    def save_user_info(self, name, sex, age):
        self.user_data.insert_multiple([
            {'name': name},
            {'sex': sex},
            {'age': age}
        ])

    def get_user_info(self):
        return self.user_data.all()
