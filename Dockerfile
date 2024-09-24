FROM ubuntu:22.04

RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    pkg-config

RUN apt-get install -y \
    mysql-server \
    libmysqlclient-dev \
    build-essential

COPY . .

RUN pip3 install -r app/requirements.txt

COPY init.sh /usr/local/bin/init.sh
RUN chmod +x /usr/local/bin/init.sh
ENTRYPOINT ["/usr/local/bin/init.sh"]

EXPOSE 5000
EXPOSE 3306

WORKDIR /app

CMD ["python3", "app.py"]
