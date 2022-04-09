FROM openjdk:11-jdk-slim

RUN mkdir /app
COPY ./target/slurm-job-response-service-*.jar /app/app.jar

WORKDIR /app
EXPOSE 8080
ENTRYPOINT ["java", "-jar", "app.jar"]