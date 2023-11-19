import datetime
import hashlib
import json
from typing import Optional
from pathlib import Path
from app.model.vocabulary_data import VocabularyData


class FileInit:

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
        self.starter_results = FileTools(path=self.starter_path,
                                         exist=True,
                                         checksums=True,
                                         )
        self.starter_exist = self.starter_results.exist
        self.starter_checksum_ok = self.check_starter_checksum()

        # checking TOLEARN
        self.to_learn_path = VocabularyData.TOLEARN
        self.to_learn_results = FileTools(path=self.to_learn_path,
                                          exist=True,
                                          )
        self.to_learn_exist = self.to_learn_results.exist

        # checking INHAND
        self.hand_path = VocabularyData.INHAND
        self.hand_results = FileTools(path=self.hand_path,
                                      exist=True,
                                      json_length=True,
                                      json_key=True,
                                      )
        self.hand_length = self.hand_results.json_length
        self.hand_stars_count_ok = self.check_hand_stars_count()

        # checking MASTERED
        self.mastered_path = VocabularyData.MASTERED
        self.mastered_results = FileTools(path=self.mastered_path,
                                          exist=True,
                                          json_length=True,
                                          )
        self.mastered_exist = self.mastered_results.exist

        # checking SETTINGS
        self.settings_path = VocabularyData.SETTINGS
        self.settings_results = FileTools(path=self.settings_path,
                                          exist=True,
                                          json_length=True,
                                          )
        self.settings_exist = self.settings_results.exist

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

            # check stars if between HAND_MIN_STARS and HAND_MAX_STARS:
            _stars_count = [s.get('stars') for s in hand_json]
            if min(_stars_count) >= self.HAND_MIN_STARS and max(_stars_count) <= self.HAND_MAX_STARS:
                return True
        return False

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

        with open('file_init.txt', 'a') as f:
            f.write(f'{_results}\n')


class FileTools:

    ALGORITHMS = {'sha1', 'md5', 'sha256', 'sha512', 'asa'}

    def __init__(self,
                 path: Path | str,
                 exist=False,
                 checksums=False,
                 json_length=False,
                 json_key=False,
                 ):

        self.path = Path(path)
        self.do_exist = exist
        self.do_checksums = checksums
        self.do_json_length = json_length
        self.do_json_key = json_key

        self.exist = None
        if self.do_exist:
            self.exist = self._exist()

        self.checksums = None
        if self.do_checksums:
            self.checksums = self._checksums()

        self.json_length = None
        if self.do_json_length:
            self.json_length = self._json_length()

    def __repr__(self):
        return f'{self.path.name}'

    def __str__(self):
        return f'{self.path.name}'

    def _exist(self) -> bool:
        """
        Check self.path existence
        :return: True | False
        """
        return self.path.exists()

    def _checksums(self) -> Optional[dict[str]]:
        """
        Generate file checksums for all available algorithms from self.ALGORITHMS
        returning dict with algo name as a key and checksum as a value
        :return: dict[str] | None
        """
        _return = {}
        if not self.exist:
            return None

        with open(self.path, 'rb') as f:
            _data = f.read()

        # generate file hashes described in self.ALGORITHMS if they available
        for algorithm in self.ALGORITHMS & hashlib.algorithms_available:
            _return[algorithm] = hashlib.new(algorithm, _data).hexdigest()
        return _return

    def _json_length(self) -> Optional[int]:
        """
        Return json data length, None if fault
        :return: int | None
        """
        if not self.exist:
            return None

        # try if given file is valid json format, return None otherwise
        try:
            with open(self.path) as f:
                _json = json.load(f)
        except json.decoder.JSONDecodeError:
            return None

        # try to establish length of the json if ValueError return None
        try:
            _length = len(_json)
            return _length
        except ValueError:
            return None


if __name__ == '__main__':
    file_init = FileInit()
