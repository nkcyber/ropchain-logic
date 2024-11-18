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
# This adds all files and sets appropriate permissions.
# Note that it's important for "example" to be a root-owned Set-UID binary,
# and for "flag.txt" to be only accessible as root.
RUN chmod 400 flag.txt && \
	chown user attack.py && \
	chgrp user attack.py && \
	cp example example-crash && \
	chmod 4755 example && \
	chmod +x *.py

## These files are expected to be supplied via volumes,
## such as via docker-compose.yml
COPY SETUP.sh SETUP.sh
COPY SETUP_FILES SETUP_FILES/
RUN bash SETUP.sh
RUN rm SETUP.sh
RUN rm -rf SETUP_FILES/

USER user

CMD ["/bin/bash"]

