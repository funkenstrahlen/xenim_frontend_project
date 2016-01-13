

class ReadWriteDatabase(object):
    DATABASES = {
        'default': {
            # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or
            # 'oracle'.
            'ENGINE': 'django.db.backends.sqlite3',
            # Or path to database file if using sqlite3.
            'NAME': 'dev.sqlite',
            # Not used with sqlite3.
            'USER': '',
            # Not used with sqlite3.
            'PASSWORD': '',
            # Set to empty string for localhost. Not used with sqlite3.
            'HOST': '',
            # Set to empty string for default. Not used with sqlite3.
            'PORT': '',
        }
    }

    @property
    def INSTALLED_APPS(self):
        return super(ReadWriteDatabase, self).INSTALLED_APPS

    @property
    def MIDDLEWARE_CLASSES(self):
        return super(ReadWriteDatabase, self).MIDDLEWARE_CLASSES
