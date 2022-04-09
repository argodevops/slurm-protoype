package uk.co.deep3.slurmjobresponseservice.controller;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

@RestController
public class JobResponseController {

    private static Logger logger = LoggerFactory.getLogger(JobResponseController.class);

    @GetMapping("/info")
    public String info() {
        return "Slurm Job Response app";
    }

    @PostMapping("/job/postJob")
    public @ResponseBody
    ResponseEntity<String> postJob(@RequestBody byte[] response) {
        logger.info("Received response: " + new String(response));
        return new ResponseEntity<>("success", HttpStatus.OK);
    }
}
