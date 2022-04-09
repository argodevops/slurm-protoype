import pytest
from compute.flows import *

@pytest.fixture
def job_response():
    return {
        "return_uri": "http://localhost:8080",
        "status": "COMPLETED",
        "payload": "Processing success"
    }

@pytest.fixture
def job_request():
    return {
        "run_duration": "2",
        "process": {
            "name": "TESTXX",
        }
    }

@pytest.mark.flows
def test_flow_a(job_request, job_response):
    """
    Test flow A processing, return the response unchanged
    """
    flow_a = TestA()
    flow_response = flow_a.process(job_request, job_response)
    assert flow_response['status'] == 'COMPLETED'
    assert flow_response['payload'] == 'Processing success'

@pytest.mark.flows
def test_flow_b(job_request, job_response):
    """
    Test flow B processing, return a failed response
    """
    flow_b = TestB()
    flow_response = flow_b.process(job_request, job_response)
    assert flow_response['status'] == 'FAILED'
    assert flow_response['payload'] == 'Processing failed'

@pytest.mark.flows
def test_flow_c(job_request, job_response):
    """
    Test flow C processing, return the response omitting the payload
    """
    flow_c = TestC()
    flow_response = flow_c.process(job_request, job_response)
    assert flow_response['status'] == 'COMPLETED'
    assert 'payload' not in flow_response

