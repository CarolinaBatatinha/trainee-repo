    FROM python:3.8
    WORKDIR /app/
    RUN pip install boto3 pandas
    COPY movies.csv series.csv script.py /app/
    CMD ["python", "script.py"]