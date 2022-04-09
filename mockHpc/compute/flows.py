"""
All test flow processing logic must reside in this file.
"""

class BaseFlow(object):
    """
    Base flow processing class, no processing
    """
    def process(self, request: dict, response: dict) -> dict:
        return response


class TestA(BaseFlow):
    """
    Apply TestA flow processing logic, no processing
    """
    def process(self, request: dict, response: dict) -> dict:
        return super().process(request, response)


class TestB(BaseFlow):
    """
    Apply TestB flow processing logic, failed response
    """
    def process(self, request: dict, response: dict) -> dict:
        response['status'] = 'FAILED'
        response['payload'] = 'Processing failed'
        return response


class TestC(BaseFlow):
    """
    Apply TestC flow processing logic, delete payload from response
    """
    def process(self, request: dict, response: dict) -> dict:
        del response['payload']
        return response
