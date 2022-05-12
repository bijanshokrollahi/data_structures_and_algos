#!/usr/bin/env python3

import codecs
import string
import sys
import time

from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.hashes import SHA1
from cryptography.hazmat.primitives.twofactor.totp import TOTP


ONE_WEEK_IN_SECONDS = 604_800


def generate_secret():
    totp = TOTP(
        key=codecs.encode(string.ascii_letters, encoding="utf-8"),
        length=8,
        algorithm=SHA1(),
        time_step=ONE_WEEK_IN_SECONDS,
        backend=default_backend(),
    )
    seed = int(time.time())
    token = codecs.decode(totp.generate(seed), encoding="utf-8")
    return f"{token}-{seed}"


# there are 2 small bugs below you'll have to fix before proceeding :)
if __name__ == "__main__":
    print(f"Please go to https://ramp.com/careers and use this secret when ")
    secret = generate_secret()
    print(f"you apply: {secret}")
