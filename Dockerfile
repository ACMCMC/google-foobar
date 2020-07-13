FROM python:3
ADD /src /
RUN pip install requests
RUN pip install beautifulsoup4
RUN pip install progressbar2
RUN pip install selenium
CMD ["python", "run.py"]