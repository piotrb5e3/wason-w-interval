import csv


def export(filename, storage):
    try:
        with open(filename, mode='w', newline='') as f:
            e = _Exporter(f, storage)
            e.export()
    except (IOError, OSError) as e:
        raise ExportException(str(e))


class ExportException(Exception):
    pass


EXPERIMENT_SETTINGS_HEADERS = [
    'experiment mode',
    'interval generation training session length',
    'interval generation measuring session length',
    'card selection training session length',
    'interval generation no-clicking timeout', ]
CARD_SELECTION_DESCRIPTION_HEADERS = [
    'number', 'is training', 'rule', 'card 1 text', 'card 2 text',
    'card 3 text', 'card 4 text']
USER_DATA_HEADERS = ['name', 'sex', 'age']
CLICK_TIMES_HEADERS = ['time']
CARD_SELECTION_HEADERS = ['external number', 'number', 'total_time',
                          'solving_time', 'positions', 'selected']
BUTTON_TOGGLES_HEADERS = ['button', 'time']

MEASURING_SESSION = 0


class _Exporter(object):
    csvwriter = None
    storage = None

    def __init__(self, file, storage):
        self.csvwriter = csv.writer(file)
        self.storage = storage

    def export(self):
        self.export_experiment_settings()
        self.export_user_data()
        self.export_measuring_session()
        self.export_selection_experiments()

    def export_experiment_settings(self):
        self.csvwriter.writerow(EXPERIMENT_SETTINGS_HEADERS)
        exp_settings = self.storage.get_experiment_config()
        self.csvwriter.writerow(
            [exp_settings['mode'],
             exp_settings['ig_training_session_time'],
             exp_settings['ig_measuring_session_time'],
             exp_settings['ig_w_selection_training_session_time'],
             exp_settings['ig_no_clicking_warning_time'], ])

        self.csvwriter.writerow([])
        self.csvwriter.writerow(CARD_SELECTION_DESCRIPTION_HEADERS)
        for cs in exp_settings['card_selections']:
            self.csvwriter.writerow([
                cs['number'], cs['is_fixed_position'], cs['rule'],
                cs['cards'][0], cs['cards'][1], cs['cards'][2], cs['cards'][3],
            ])

    def export_user_data(self):
        self.csvwriter.writerow([])
        self.csvwriter.writerow(USER_DATA_HEADERS)
        user_data = {}
        for d in self.storage.get_user_info():
            for key in d:
                user_data[key] = d[key]
        self.csvwriter.writerow(
            [user_data['name'], user_data['sex'], user_data['age']])

    def export_measuring_session(self):
        self.csvwriter.writerow([])
        self.csvwriter.writerow(CLICK_TIMES_HEADERS)
        clicks = self.storage.get_clicks_from(MEASURING_SESSION)
        for click in clicks:
            self.csvwriter.writerow([click['time']])

    def export_selection_experiments(self):
        exp_settings = self.storage.get_experiment_config()
        for i in range(len(exp_settings['card_selections'])):
            self.export_single_experiment(i + 1)

    def export_single_experiment(self, expno):
        self.csvwriter.writerow([])
        self.csvwriter.writerow(CARD_SELECTION_HEADERS)
        exp_data = self.storage.get_cs_result(expno)
        selected = []
        for k in exp_data['status']:
            if exp_data['status'][k]:
                selected.append(k)
        selected.sort()

        permutation = ['1', '2', '3', '4']

        for k in exp_data['positions']:
            permutation[exp_data['positions'][k]] = str(k)

        solving_time = exp_data['total_time'] - exp_data['solving_start_time']

        self.csvwriter.writerow(
            [expno, exp_data['number'], exp_data['total_time'],
             solving_time, ':'.join(permutation), ':'.join(selected)])

        self.csvwriter.writerow([])
        self.csvwriter.writerow(CLICK_TIMES_HEADERS)
        clicks = self.storage.get_clicks_from(expno)
        for click in clicks:
            self.csvwriter.writerow([click['time']])

        self.csvwriter.writerow([])
        self.csvwriter.writerow(BUTTON_TOGGLES_HEADERS)
        toggles = self.storage.get_toggles_from(expno)
        for toggle in toggles:
            self.csvwriter.writerow(
                [toggle['button'],
                 toggle['time'] - exp_data['solving_start_time']]
            )
