FROM python:3.9

RUN apt-get update && apt-get install -y gcc ssh openssh-server gettext postgresql-client libpq-dev \
    libjpeg-dev libopenjp2-7-dev wget zsh

RUN mkdir /app/

WORKDIR /app

COPY ./flask-app/ /app/
COPY ./docker-entrypoint.sh /app/
RUN ls
RUN pip install -r requirements.txt

RUN mkdir /var/run/sshd

RUN wget https://github.com/robbyrussell/oh-my-zsh/raw/master/tools/install.sh -O - | zsh || true

RUN echo "cd /flask-app/app" >> /root/.zshrc
