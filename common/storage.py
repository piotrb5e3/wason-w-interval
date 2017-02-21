from tinydb import TinyDB, Query


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

    def get_cs_result(self, expno):
        r = self.selections.search(Query().expno == expno)
        return r[0]

    def save_user_info(self, name, sex, age):
        self.user_data.insert_multiple([
            {'name': name},
            {'sex': sex},
            {'age': age}
        ])

    def save_experiment_config(self, config, mode):
        card_selections = [
            {
                'number': cs.number,
                'is_fixed_position': cs.is_fixed_position,
                'text_p1': cs.text_p1,
                'rule': cs.rule,
                'text_p2': cs.text_p2,
                'instructions': cs.instructions,
                'cards': [c.text for c in cs.cards],
            } for cs in config.card_selections]

        self.experiment_data.insert({
            'mode': mode,
            'ig_training_session_time': config.ig_training_session_time,
            'ig_measuring_session_time': config.ig_measuring_session_time,
            'ig_w_selection_training_session_time': config.ig_w_selection_training_session_time,
            'ig_no_clicking_warning_time': config.ig_no_clicking_warning_time,

            'welcome_text': config.welcome_text,
            'ig_instructions_text': config.ig_instructions_text,
            'ig_pre_measuring_session_text': config.ig_pre_measuring_session_text,
            'ig_w_selection_instructions_text': config.ig_w_selection_instructions_text,
            'pre_experiment_text': config.pre_experiment_text,
            'thanks_text': config.thanks_text,
            'cs_instructions_short': config.cs_instructions_short,
            'card_selections': card_selections,
        })

    def get_experiment_config(self):
        return self.experiment_data.all()[0]

    def get_user_info(self):
        return self.user_data.all()

    def get_clicks_from(self, expno):
        return self.clicks.search(Query().expno == expno)

    def get_toggles_from(self, expno):
        return self.button_toggles.search(Query().expno == expno)

    def save_completed_experiment(self):
        self.integrity.insert({'complete': True})
