FROM python:3.6.6-alpine
COPY k8 /app
WORKDIR /app
RUN pip3 install -r dependencias.txt && \
    python3 -m textblob.download_corpora
EXPOSE 5000
ENTRYPOINT ["python3"]
CMD ["primos_bench.py"]
