FROM python

COPY /tested /to_docker

WORKDIR /tested

RUN make install; make run

