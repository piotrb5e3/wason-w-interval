def export(filename, storage):
    try:
        with open(filename, mode='w') as f:
            e = _Exporter(f, storage)
            e.export()
    except (IOError, OSError) as e:
        raise ExportException(str(e))


class ExportException(Exception):
    pass


class _Exporter(object):
    file = None
    storage = None

    def __init__(self, file, storage):
        self.file = file
        self.storage = storage

    def export(self):
        self.export_experiment_settings()
        self.export_user_data()
        self.export_measuring_session()
        self.export_selection_experiments()

    def export_experiment_settings(self):
        pass

    def export_user_data(self):
        pass

    def export_measuring_session(self):
        pass

    def export_selection_experiments(self):
        pass

    def export_single_experiment(self, expno):
        pass
