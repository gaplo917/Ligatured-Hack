FROM gaplo917/docker-python-fontforge

WORKDIR /usr/src/app

COPY . ./

RUN mkdir -p fonts/output

ENTRYPOINT ["make"]
