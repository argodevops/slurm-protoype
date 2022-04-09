from __future__ import annotations
import json


class Job(object):
    """A Job class for wrapping the job request and response
    """

    def __init__(self, data: Job) -> None:
        """
        Creates a Job and splits request and response from the data
        :param data: The job request data
        """
        self.__dict__ = json.loads(data)
        self.return_url = self.__dict__["request"]["response"].pop('return_url')
        self.response = self.__dict__["request"].pop("response")
        self.request = self.__dict__["request"]

    @staticmethod
    def parse(filename: str) -> Job:
        """
        Parses a file and builds it onto a Job object
        :param filename:  The file to parse
        :return: A Job object
        """
        if filename is not None:
            with open(filename, 'r') as f:
                request = Job(f.read())
        else:
            raise Exception('Request filename not provided')
        return request

    def __str__(self) -> str:
        return "{} {}".format(self.__class__, self.__dict__)
