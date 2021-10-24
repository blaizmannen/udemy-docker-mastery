FROM python:3

WORKDIR /

COPY cpu_usage.py cpu_usage.py

RUN pip install psutil

CMD [ "python", "cpu_usage.py", ">result.txt" ]