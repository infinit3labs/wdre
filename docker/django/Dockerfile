FROM revolutionsystems/python:3.6.3-wee

WORKDIR /app

ENV PYTHONUNBUFFERED 1
RUN pip install --upgrade pip setuptools

COPY requirements.txt /tmp/requirements.txt
RUN pip install --upgrade --no-cache-dir -r /tmp/requirements.txt

COPY docker/django/entrypoint.sh /usr/local/bin/entrypoint.sh
RUN chmod +x /usr/local/bin/entrypoint.sh
ENTRYPOINT ["entrypoint.sh"]