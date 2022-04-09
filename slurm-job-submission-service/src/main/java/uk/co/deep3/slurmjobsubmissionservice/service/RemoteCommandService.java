package uk.co.deep3.slurmjobsubmissionservice.service;

import org.springframework.beans.factory.annotation.Value;
import org.springframework.stereotype.Service;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.FileWriter;
import java.util.Random;
import java.util.UUID;
import java.util.logging.Logger;

@Service
public class RemoteCommandService {

    @Value("${container.id}")
    private String containerId;

    @Value("${file.output.path}")
    private String fileOutputPath;

    @Value("${slurm.file.location}")
    private String slurmFileLocation;

    @Value("${slurm.server.address}")
    private String slurmServerAddress;

    @Value("${scp.port}")
    private int scpPort;

    private static final Logger LOG = Logger.getLogger(RemoteCommandService.class.getName());

    public void sendJobRequestToRemoteServer(String jobRequest) {
        UUID uuid = UUID.randomUUID();
        String jobSubmissionFileName = "jobRequest-" + uuid.toString()  + ".json";
        String localSubmissionFilePath = fileOutputPath + "/" + jobSubmissionFileName;
        writeRequestToFile(jobRequest, localSubmissionFilePath);

        String copyFileRequest = String.format("docker cp %s %s:%s", localSubmissionFilePath, containerId, slurmFileLocation);
        //String copyFileRequest = String.format("scp %s %s:%s", localSubmissionFilePath, slurmServerAddress, slurmFileLocation);
        runCommand(copyFileRequest);

        String submitSlurmJobRequest = String.format("docker exec -d %s sbatch --wrap=\"python3.8 /app/main.py --jobid=%s --filename=%s\"", containerId, uuid, slurmFileLocation + jobSubmissionFileName);
        //String submitSlurmJobRequest = String.format("sbatch --wrap=\"python3.8 ~/mockHpc/main.py --jobid=%s --filename=%s\"", uuid, slurmFileLocation + "/" + jobSubmissionFileName);
        //String sshCommand = String.format("ssh %s -t %s", slurmServerAddress, submitSlurmJobRequest);
        //runCommand(sshCommand);
        runCommand(submitSlurmJobRequest);
    }

    private void runCommand(String command) {
        LOG.info(command);
        try {
            Process process = Runtime.getRuntime().exec(command);
            BufferedReader processReader = new BufferedReader(new InputStreamReader(process.getInputStream()));

            processReader.lines().forEach(LOG::info);
            processReader.close();
        } catch (IOException e) {
            throw new RuntimeException(e);
        }
    }

    private void writeRequestToFile(String request, String fileName) {
        try (FileWriter jobRequestFile = new FileWriter(fileName)){
            jobRequestFile.write(request);
        } catch (IOException e) {
            throw new RuntimeException(e);
        }
    }
}
