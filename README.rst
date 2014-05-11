django_runprocess
=================

This app allows you to run external applications along with the ``runserver``
command. This is useful for example to run automatic compilation of your
sass/less files without having to manually run ``sass --watch``.

Installation
============

``pip install django_runprocess``

Configuration
=============

Add it to your ``INSTALLED_APPS``::

    INSTALLED_APPS = (
        ...
        'runprocess'
    )

Add the commands you want to be executed in the ``RUNPROCESS_PROCESSES``
setting.  For example, to automatically run ``sass --watch`` along with
``runserver``, use the following::

    SASS_DIR = os.path.join(STATIC_ROOT, 'sass')
    CSS_DIR = os.path.join(STATIC_ROOT, 'css')

    RUNPROCESS_PROCESSES = (
        ('sass', '--watch', '%s:%s' % (SASS_DIR, CSS_DIR)),
    )
