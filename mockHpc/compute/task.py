import time
import requests
from logging import Logger
from compute.flows import *
from parse.request import *


class Task(object):
    # statics
    run_duration = "run_duration"
    process = "process"
    process_name = "name"

    def __init__(self, log : Logger) -> None:
        """
        Creates a Task object
        :param log: The logger handle
        """
        self.log = log

    @staticmethod
    def get_flow_processing(name='BaseFlow'):
        flows = {
            'BaseFlow': BaseFlow(),
            'TESTA': TestA(),
            'TESTB': TestB(),
            'TESTC': TestC()
            # Add additional test flows here
        }
        return flows.get(name, BaseFlow())

    @staticmethod
    def execute(data: Job, log: Logger) -> None:
        """
        Executes the processing logic
        :param data: The processing data
        :param log: The logger handle
        """
        task = Task(log)
        # run through steps to simulate/mock the flow processing
        task.run(data)

    def run(self, data: Job) -> None:
        """
        Simulates the task processing
        :param data: The processing data
        """
        try:
            request = data.request
            response = data.response
            if Task.process in request:
                if Task.process_name in request[Task.process]:
                    flow_name = request[Task.process][Task.process_name]
            # Execute flow processing
            flow_processing = Task.get_flow_processing(flow_name)
            self.log.info(f'Processing flow: {flow_processing.__class__}')
            response = flow_processing.process(request, response)
            # Simulate run duration
            if Task.run_duration in request:
                time.sleep(int(request[Task.run_duration]))
            # Send response
            self.send_response(data.return_url, response)
        except Exception as e:
            self.log.error(f'Processing failed: {e}')

    def send_response(self, url, response) -> None:
        """
        Sends the HTTP response
        """
        self.log.info(f'Send response: {response} to url: {url}')
        http_resp = requests.post(url, json=response)
        if http_resp.status_code != 200:
            self.log.error(f'Failed to send response: {http_resp}')
