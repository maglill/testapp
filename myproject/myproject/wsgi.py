"""
WSGI config for myproject project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/wsgi/
"""

import os
#OSモジュールのインポート → Python上で書かれたコードをどのOSでも動くようにするため。

from dj_static import Cling
#Clingをimport。
from django.core.wsgi import get_wsgi_application
#get_wsgi_applicationをimport。

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myproject.settings")

application = Cling(get_wsgi_application())