FROM python:3
ADD /src /
RUN pip install requests
RUN pip install beautifulsoup4
CMD ["python", "run.py"]