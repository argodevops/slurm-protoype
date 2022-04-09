#!/usr/bin/env python
from parse import request
from compute import task
import argparse
import utils

# read command line opts
parser = argparse.ArgumentParser()
parser.add_argument("-f", "--filename", metavar="FILE", help="The JSON request filename to process")
parser.add_argument("-j", "--jobid", help="The unique jobid")
args = parser.parse_args()

# create logger
log = utils.create_logger(args.jobid)
log.info(f'Job {args.jobid} start')

# parse job request
log.info(f'Parsing request: {args.filename}')
data = request.Job.parse(args.filename)

# compute response
log.info(f'Processing request: {data.request}')
task.Task.execute(data, log)

log.info(f'Job {args.jobid} complete')