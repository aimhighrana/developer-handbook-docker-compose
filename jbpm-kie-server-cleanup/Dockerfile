FROM python:3.9.12
RUN apt-get update
COPY ./requirement.txt .
COPY ./init.py .
RUN pip install -r requirement.txt
ENTRYPOINT ["python3","init.py"]
