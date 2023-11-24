import datetime


class FileInitView:

    def __init__(self,
                 logging_on_screen=False,
                 logging_to_file=False,
                 logging_filepath=None):
        self.logging_on_screen = logging_on_screen
        self.logging_to_file = logging_to_file
        self.logging_filepath = logging_filepath
        self.timestamp = datetime.datetime.strftime(datetime.datetime.now(),
                                                    '%Y-%m-%d %H:%M:%S.%f',
                                                    )

    def _log_me(self, _msg):
        if self.logging_on_screen:
            print(f'[{self.timestamp}] {_msg}')
        if self.logging_to_file and self.logging_filepath:
            with open(self.logging_filepath, 'a') as f:
                f.write(f'[{self.timestamp}] {_msg}\n')

    def starter_missing_or_corrupted(self):
        _msg = 'STARTER missing or corrupted'
        self._log_me(_msg)

    def some_files_missing(self):
        _msg = 'Some files missing'
        self._log_me(_msg)

    def all_files_ok(self):
        _msg = 'All files OK'
        self._log_me(_msg)

    def first_run(self):
        _msg = 'First run, files created'
        self._log_me(_msg)
