import hashlib
import json
from typing import Optional
from pathlib import Path


class FileInitModel:
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

