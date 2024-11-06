FROM python:3.12

RUN apt update && \
	apt install --assume-yes --no-install-recommends --quiet \
		libc6-dev-i386 \
		gcc-multilib \
		vim \
		gdb \
		build-essential \
		make \
	 && apt-get clean all

WORKDIR /app

COPY requirements.txt .
RUN pip3 install -r requirements.txt

COPY example.c .
# RUN gcc -no-pie -fno-stack-protector -z execstack -static example.c -o example
# RUN gcc -m32 -fno-stack-protector -z execstack example.c -o example
RUN make


COPY attack.py .

CMD ["/bin/sh"]

