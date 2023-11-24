import datetime
import hashlib
import json
from app.model.vocabulary_data import VocabularyData
from app.model.file_init import FileInitModel
from app.view.file_init import FileInitView


class FileInitController:
    LOGGING_ON_SCREEN = True
    LOGGING_TO_FILE = True
    LOGGING_FILEPATH = '../../logs/log_file_init.txt'

    LOGGING_RESULTS_FILEPATH = 'logs/log_results.txt'

    STARTER_MD5_SUM = '8737a00c0deac85c47b77b4697f2ec16'
    STARTER_SHA1_SUM = '0e79af375bb0b75f5c1910c935c5b91185d85aac'
    STARTER_SHA256_SUM = 'b138cbdcc4501f6eb769811c71408392144569281815116c7a60c31bb49e1f95'

    TO_LEARN = None

    HAND_MIN_STARS = 0
    HAND_MAX_STARS = 6

    MASTERED = None

    SETTINGS = None

    def __init__(self):
        # checking STARTER
        self.starter_path = VocabularyData.STARTER
        self.starter_results = FileInitModel(path=self.starter_path,
                                             exist=True,
                                             checksums=True,
                                             )
        self.starter_exist = self.starter_results.exist
        self.starter_checksum_ok = self.check_starter_checksum()

        # checking TOLEARN
        self.to_learn_path = VocabularyData.TOLEARN
        self.to_learn_results = FileInitModel(path=self.to_learn_path,
                                              exist=True,
                                              )
        self.to_learn_exist = self.to_learn_results.exist

        # checking INHAND
        self.hand_path = VocabularyData.INHAND
        self.hand_results = FileInitModel(path=self.hand_path,
                                          exist=True,
                                          json_length=True,
                                          json_key=True,
                                          )
        self.hand_exist = self.hand_results.exist
        self.hand_length = self.hand_results.json_length
        self.hand_stars_count_ok = self.check_hand_stars_count()
        # TODO: check for non-empty strings

        # checking MASTERED
        self.mastered_path = VocabularyData.MASTERED
        self.mastered_results = FileInitModel(path=self.mastered_path,
                                              exist=True,
                                              json_length=True,
                                              )
        self.mastered_exist = self.mastered_results.exist

        # checking SETTINGS
        self.settings_path = VocabularyData.SETTINGS
        self.settings_results = FileInitModel(path=self.settings_path,
                                              exist=True,
                                              json_length=True,
                                              )
        self.settings_exist = self.settings_results.exist

        # checking first run
        self.is_first_run = None
        self.check_first_run()

        # results
        self.save_results()

    def check_starter_checksum(self) -> bool:
        # iterate all class attributes starting with 'STARTER' and ending with 'SUM'
        for starter_sum in [a for a in dir(self) if a.startswith('STARTER') and a.endswith('SUM')]:
            # if any of hard-coded class attributes sums are not equal to calculated one return False
            if not getattr(self, starter_sum) == self.starter_results.checksums.get(starter_sum.split('_')[1].lower()):
                return False
        return True

    def check_hand_stars_count(self):
        if self.hand_results.exist:
            with open(self.hand_path) as f:
                hand_json = json.load(f)

            try:
                # check stars if between HAND_MIN_STARS and HAND_MAX_STARS:
                _stars_count = [s.get('stars') for s in hand_json]
                if min(_stars_count) >= self.HAND_MIN_STARS and max(_stars_count) <= self.HAND_MAX_STARS:
                    return True
            except ValueError:
                pass

            return False

    def check_first_run(self):
        # first run: only STARTER file exist
        if self.starter_exist and self.starter_checksum_ok:

            if all([self.settings_exist,
                    self.mastered_exist,
                    self.to_learn_exist,
                    self.hand_exist]):
                # all files exist, not the first run
                self.is_first_run = False
                FileInitView(logging_on_screen=self.LOGGING_ON_SCREEN,
                             logging_to_file=self.LOGGING_TO_FILE,
                             logging_filepath=self.LOGGING_FILEPATH,
                             ).all_files_ok()

            elif all([not self.settings_exist,
                      not self.mastered_exist,
                      not self.to_learn_exist,
                      not self.hand_exist]):
                # none files exist, first run, create files
                self.is_first_run = True
                self._create_to_learn_file()
                self._create_hand_file()
                self._create_mastered_file()
                self._create_settings_file()

                FileInitView(logging_on_screen=self.LOGGING_ON_SCREEN,
                             logging_to_file=self.LOGGING_TO_FILE,
                             logging_filepath=self.LOGGING_FILEPATH,
                             ).first_run()

            else:
                FileInitView(logging_on_screen=self.LOGGING_ON_SCREEN,
                             logging_to_file=self.LOGGING_TO_FILE,
                             logging_filepath=self.LOGGING_FILEPATH,
                             ).some_files_missing()

        else:
            FileInitView(logging_on_screen=self.LOGGING_ON_SCREEN,
                         logging_to_file=self.LOGGING_TO_FILE,
                         logging_filepath=self.LOGGING_FILEPATH,
                         ).starter_missing_or_corrupted()

    def _create_to_learn_file(self):
        with open(self.starter_path, 'r') as f:
            _content = f.read()
        with open(self.to_learn_path, 'w') as f:
            f.write(_content)

    def _create_hand_file(self):
        with open(self.hand_path, 'w') as f:
            f.write('""')

    def _create_mastered_file(self):
        with open(self.mastered_path, 'w') as f:
            f.write('""')

    def _create_settings_file(self):
        with open(self.settings_path, 'w') as f:
            f.write('{"date": "0000-00-00"}')

    def save_results(self):
        _timestamp = datetime.datetime.now()

        _results = {'TIMESTAMP': {'date': datetime.datetime.strftime(_timestamp, '%Y-%m-%d'),
                                  'time': datetime.datetime.strftime(_timestamp, '%H:%M:%S'),
                                  'ms': datetime.datetime.strftime(_timestamp, '%f'),
                                  },
                    'STARTER': {'name': str(self.starter_results),
                                'exist': self.starter_results.exist,
                                'checksum_ok': self.starter_checksum_ok,
                                },
                    'TOLEARN': {'name': str(self.to_learn_results),
                                'exist': self.to_learn_results.exist,
                                },
                    'INHAND': {'name': str(self.hand_results),
                               'exist': self.hand_results.exist,
                               'length': self.hand_results.json_length,
                               },
                    'MASTERED': {'name': str(self.mastered_results),
                                 'exist': self.mastered_results.exist,
                                 'length': self.mastered_results.json_length,
                                 },
                    'SETTINGS': {'name': str(self.settings_results),
                                 'exist': self.settings_results.exist,
                                 'length': self.settings_results.json_length,
                                 },
                    }
        # add checksum, sha1 used for shortness ;)
        _results['CHECKSUM'] = {'sha1': hashlib.sha1(f'{_results}'.encode()).hexdigest()}

        with open(self.LOGGING_RESULTS_FILEPATH, 'a') as f:
            f.write(f'{_results}\n')


if __name__ == '__main__':
    fic = FileInitController()
