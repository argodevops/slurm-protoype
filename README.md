# README #

Demonstratable Slurm prototype. 

### What is this repository for? ###

All source code for demonstratable set of applications for submitting jobs to Slurm for execution on its nodes. It consists of:
* A job submission service (spring boot app) to submit jobs to Slurm (slurmctld)
* A mockHPC app to process the job submission and send a response
* A job response service (spring boot app) to handle the response

### How do I get set up? ###

The mockHpc and response app will build into a docker image.

* docker build -t slurm-mockhpc .
* docker build -t slurm-job-response-service .

The job submission app will be run as a jar from the command line.

* mvn clean package

### How do I run it all up? ###

Run the slurm-mockHpc container which has the Slurm daemons and mockHpc app installed.

* docker run -d slurm-mockHpc

If you exec (docker exec -it slurm-mockHpc /bin/bash) into the container and run sinfo command it should show the Slurm daemons running.

Run the job response app. By default it will expose port 8080. It exposes an endpoint (http://<url>:<port>/job/postJob) which simply logs any received HTTP POST requests.

* docker run -d -p 9081:8080 slurm-job-response-service

Run the job request app. The app will use the docker exec command to fire a script (including the job request json) to the Slurm container and execute the mockHpc app, which will send a response using the provided return url.  

java -jar target/slurm-job-response-service.jar 

### Contribution guidelines ###

* Writing code and tests
    * To run the app - python mockHpc/main.py -j <jobid> -f <request.json>
        * where -j is a unique jobid and -f is a job request JSON file 
    * To run all the unit tests from the test directory - py.test
    * To run the flow logic tests - py.test -m flows
* Code review
* Pipeline successfully builds
* Build and deploy

