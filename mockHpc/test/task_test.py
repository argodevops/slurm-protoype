import pytest
from compute.task import *
from pytest_httpserver import HTTPServer

TESTB_JSON = 'data/flow_testb_request.json'


@pytest.mark.task
def test_flowb_response(httpserver: HTTPServer):
    """
    Test task logic to ensure correct response is sent
    """
    # expected http post
    httpserver.expect_request("/foobar", data='{"status": "FAILED", "payload": "Processing failed"}', method="POST").respond_with_data("example_response")

    # create job and override return url to use mock http server
    job = Job.parse(TESTB_JSON)
    job.return_url = httpserver.url_for('/foobar')
    # execute tasking on job
    Task.execute(job, Logger('test'))

    # check expected http post call
    httpserver.check_assertions()
