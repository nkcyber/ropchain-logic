FROM python:3.12

RUN apt update && \
	apt install --assume-yes --no-install-recommends --quiet \
		libc6-dev-i386 \
		gcc-multilib \
		vim \
		gdb \
		build-essential \
	 && apt-get clean all

WORKDIR /app

COPY requirements.txt .
RUN pip3 install -r requirements.txt

COPY Makefile example.c ./

RUN make

COPY attack.py attack2.py create_table.py .

## TODO: do not run this as root

CMD ["/bin/sh"]

