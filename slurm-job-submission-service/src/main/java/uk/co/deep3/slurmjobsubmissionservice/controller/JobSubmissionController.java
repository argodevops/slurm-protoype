package uk.co.deep3.slurmjobsubmissionservice.controller;

import uk.co.deep3.slurmjobsubmissionservice.service.SubmissionService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class JobSubmissionController {

    @Autowired
    SubmissionService submissionService;
    
    @PostMapping("/request")
    public void submitJobToSlurm(@RequestBody String jobRequest) {
        submissionService.submit(jobRequest);
    }
}
