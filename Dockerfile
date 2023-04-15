FROM python:3.10-alpine
COPY entry.py entry.py
RUN pip install backseat-driver==0.0.2
ENTRYPOINT ["entry.py"]
