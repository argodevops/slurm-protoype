package uk.co.deep3.slurmjobsubmissionservice.service;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

@Service
public class SubmissionService {

    @Autowired
    RemoteCommandService remoteCommandService;

    public void submit(String jobRequest){
        remoteCommandService.sendJobRequestToRemoteServer(jobRequest);
    }
}
