import datetime


class FileInitView:

    def __init__(self, on_screen=False, to_file=False, filename=None):
        self.on_screen = on_screen
        self.to_file = to_file
        self.filename = filename
        self.timestamp = datetime.datetime.strftime(datetime.datetime.now(),
                                                    '%Y-%m-%d %H:%M:%S.%f',
                                                    )

    def _log_me(self, _msg):
        if self.on_screen:
            print(f'[{self.timestamp}] {_msg}')
        if self.to_file and self.filename:
            with open(self.filename, 'a') as f:
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
