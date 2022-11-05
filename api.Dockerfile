# docker build . -t nesantu_api -f api.Dockerfile
# docker push nesantu_api

FROM python:3.11.0-alpine3.16
ENV PYTHONPATH=/app
WORKDIR /app

RUN apk update && apk upgrade
RUN apk add --no-cache bash \
                       build-base \
                       gcc \
                       libffi-dev \
                       linux-headers \
                       musl-dev \
                       pkgconfig \
                       python3-dev \
    && rm -rf /var/cache/apk/*

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# COPY ./ /app
COPY ./app /app

# COPY prestart.sh /app

RUN chmod +x /app/prestart.sh

CMD ["sh", "/app/prestart.sh"]
