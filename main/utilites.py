from django.core.signing import Signer  # цифровая подпись для защиты от подделки
from datetime import datetime
from os.path import splitext

signer = Signer()


def get_timestamp_path(instance, filename):
    return '%s%s' % (datetime.now().timestamp(), splitext(filename)[1])
