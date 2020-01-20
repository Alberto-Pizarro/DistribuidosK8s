FROM openjdk:8-jdk-alpine
ENV K8_PYTHON_API_URL http://localhost:5000
ADD target/calculo-primos-web-0.0.1-SNAPSHOT.jar /
EXPOSE 8080
CMD ["java", "-jar", "calculo-primos-web-0.0.1-SNAPSHOT.jar", "--k8.python.api.url=${K8_PYTHON_API_URL}"]
