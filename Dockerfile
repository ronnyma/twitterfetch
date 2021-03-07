FROM python:3

COPY main.py persistence.py cron.tab requirements.txt ./

ADD cron.tab /etc/cron.d/cron.tab
RUN pip install --no-cache-dir -r requirements.txt && chmod +x ./main.py && chmod 0644 /etc/cron.d/cron.tab && touch /var/log/cron.log && apt-get update && apt-get -y install cron && crontab /etc/cron.d/cron.tab

CMD cron && tail -f /var/log/cron.log


