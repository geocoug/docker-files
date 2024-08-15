FROM python:3.12-slim

ENV HOME=/app
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR $HOME

# hadolint ignore=DL3008
RUN apt-get update -y \
    && apt-get install --no-install-recommends -y wget \
    && rm -rf /var/lib/apt/lists/*

ADD --chmod=755 https://astral.sh/uv/install.sh /install.sh

RUN /install.sh \
    && rm /install.sh

COPY ./requirements.txt /tmp/requirements.txt

RUN $HOME/.cargo/bin/uv pip install --system --no-cache -r /tmp/requirements.txt \
    && rm -rf /tmp/requirements.txt

COPY ./main.py $HOME/main.py

RUN addgroup --system app \
    && adduser --system --group app \
    && chown -R app:app $HOME

USER app

ENTRYPOINT [ "python", "main.py" ]
