from tinydb import TinyDB


class Storage(object):
    db = None
    experiment_data = None
    user_data = None
    clicks = None
    selections = None
    button_toggles = None
    integrity = None

    def __init__(self, filename):
        self.db = TinyDB(filename)
        self.experiment_data = self.db.table('exp_data')
        self.user_data = self.db.table('user_data')
        self.clicks = self.db.table('clicks')
        self.selections = self.db.table('selections')
        self.button_toggles = self.db.table('toggles')
        self.integrity = self.db.table('integrity')

    def has_data(self):
        return len(self.user_data) > 0

    def has_complete_data(self):
        return len(self.integrity) > 0

    def purge(self):
        self.db.purge_table('exp_data')
        self.db.purge_table('user_data')
        self.db.purge_table('clicks')
        self.db.purge_table('selections')
        self.db.purge_table('toggles')
        self.db.purge_table('integrity')

    def save_experiment_click(self, time, expno):
        self.clicks.insert({'expno': expno, 'time': time})

    def save_card_click(self, expno, time, button_number):
        self.button_toggles.insert(
            {'expno': expno, 'time': time, 'button': button_number})

    #
    # Positions and status are dictionaries:
    # postitions[1:4] \in [0:3]
    # status[1:4] \in {True, False}
    #
    def save_selection_results(self, expno, number, solving_start_time,
                               total_time, positions, status):
        self.selections.insert(
            {
                'expno': expno,
                'number': number,
                'solving_start_time': solving_start_time,
                'total_time': total_time,
                'positions': positions,
                'status': status,
            }
        )

    def save_user_info(self, name, sex, age):
        self.user_data.insert_multiple([
            {'name': name},
            {'sex': sex},
            {'age': age}
        ])

    def get_user_info(self):
        return self.user_data.all()

    def save_completed_experiment(self):
        self.integrity.insert({'complete': True})
