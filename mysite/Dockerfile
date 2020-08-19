# Ubuntu 20.04 LTS
FROM ubuntu:20.04

# Install python 3.8.2
RUN apt-get update \
  && apt-get install -y python3-pip python3-dev \
  python3-dev default-libmysqlclient-dev build-essential \
  && cd /usr/local/bin \
  && ln -s /usr/bin/python3 python \
  && pip3 install --upgrade pip

# setup timezone
ENV TZ=UTC
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

# Install developer tools
RUN apt-get install -y \
  tree net-tools iputils-ping netcat vim mc

WORKDIR /usr/src/app/mysite

COPY requirements.txt ./
RUN pip3 install --no-cache-dir -r requirements.txt

COPY entrypoint.sh ./

#Prevents Python from writing pyc files to disc
ENV PYTHONDONTWRITEBYTECODE 1
#Prevents Python from buffering stdout and stderr
ENV PYTHONUNBUFFERED 1

# Create a 'm' script instead of alias so it can be used also into the Dockerfile
RUN echo '#!/bin/bash\npython manage.py "$@"' > /usr/bin/m && chmod +x /usr/bin/m

#COPY . .
ENTRYPOINT [ "/usr/src/app/mysite/entrypoint.sh"]
