FROM containers.renci.org/acis/kaniko/executor:no-copy-debug as kaniko
FROM python
USER 0
SHELL ["/bin/bash", "-c"]
ENV SHELL /bin/bash
WORKDIR /app
COPY setup.py /app
COPY --from=kaniko /kaniko /kaniko-src
RUN apt-get update
