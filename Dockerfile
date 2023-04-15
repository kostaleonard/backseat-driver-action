FROM python:3.10-alpine
COPY entry.sh entry.sh
RUN pip install backseat-driver==0.0.2
ENTRYPOINT ["entry.sh"]
