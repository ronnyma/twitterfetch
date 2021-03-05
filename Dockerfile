FROM python:3

COPY main.py persistence.py cron.tab requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

ADD cron.tab /etc/cron.d/cron.tab

RUN chmod 0644 /etc/cron.d/cron.tab

RUN touch /var/log/cron.log

RUN apt-get update
RUN apt-get -y install cron

CMD cron && tail -f /var/log/cron.log


