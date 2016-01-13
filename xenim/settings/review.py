
''' Note: always include the INSTALLED_APPS and MIDDLEWARE_CLASSES functions
          even, if you don't modify this settings
'''


class ReviewSett(object):
    @property
    def INSTALLED_APPS(self):
        return super(ReviewSett, self).INSTALLED_APPS + (
            'django_comments',
            'radioportal_review',
        )

    @property
    def MIDDLEWARE_CLASSES(self):
        return super(ReviewSett, self).MIDDLEWARE_CLASSES

    COMMENTS_APP = 'radioportal_review'
