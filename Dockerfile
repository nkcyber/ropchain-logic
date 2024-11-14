FROM python:3.12

RUN apt update && \
	apt install --assume-yes --no-install-recommends --quiet \
		libc6-dev-i386 \
		gcc-multilib \
		vim \
		gdb \
		build-essential \
		nano \
	 && apt-get clean all

WORKDIR /app

COPY requirements.txt .
RUN pip3 install -r requirements.txt

COPY Makefile example.c attack.py create_table.py flag.txt .
RUN make
RUN useradd -ms /bin/bash user
RUN chmod 400 flag.txt && \
	chmod o+r /tmp && \
	chown user attack.py && \
	chgrp user attack.py && \
	ulimit -c unlimited && \
	cp example example-crash && \
	chmod 4755 example

USER user

CMD ["/bin/bash"]

