FROM python:3.9

WORKDIR /usr/src/multi

COPY . ./

CMD ["python", "main.py"]
