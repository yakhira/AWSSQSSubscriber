ARG BUILD_FROM
FROM $BUILD_FROM

ENV WORKDIR /data
ENV APPDIR /app
ENV LANG C.UTF-8
ENV USER sqs
ENV GROUP sqs

COPY app/ $APPDIR/

WORKDIR $WORKDIR

RUN apk add --no-cache py3-pip mosquitto-clients; \
    pip install --no-cache-dir -r $APPDIR/requirements.txt; \
    addgroup $GROUP; \
    adduser -H -D -s /bin/sh -G $USER -h $WORKDIR $USER; \
    chown -R $USER:$GROUP $WORKDIR; \
    chmod +x $APPDIR/run.sh

# USER $USER

LABEL \
    io.hass.name="AWS SQS Subscriber" \
    io.hass.description="AWS SQS Subscriber." \
    io.hass.arch="${BUILD_ARCH}" \
    io.hass.type="addon" \
    io.hass.version=${BUILD_VERSION} \
    maintainer="Ruslan Iakhin <ruslan.k.yakhin@gmail.com>"

CMD ["/app/run.sh"]