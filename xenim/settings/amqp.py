

class Amqp(object):
    AMQP = False
    BROKER_HOST = "localhost"
    BROKER_PORT = 5672
    BROKER_USER = "guest"
    BROKER_PASSWORD = "guest"
    BROKER_VHOST = "/"
    BROKER_SSL = False

    @property
    def INSTALLED_APPS(self):
        return super(Amqp, self).INSTALLED_APPS

    @property
    def MIDDLEWARE_CLASSES(self):
        return super(Amqp, self).MIDDLEWARE_CLASSES + (
            'radioportal.messages.send.AMQPInitMiddleware',
        )
