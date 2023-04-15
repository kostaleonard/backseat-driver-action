FROM python:3.10-alpine
RUN pip install backseat-driver==0.0.2
ENTRYPOINT ["backseat-driver"]
