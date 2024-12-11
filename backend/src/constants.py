import os
from enum import StrEnum


COPR_BUILD_URL = "https://copr.fedorainfracloud.org/coprs/build/{0}"
KOJI_BUILD_URL = "https://koji.fedoraproject.org/koji/buildinfo?buildID={0}"
FEEDBACK_DIR = os.environ.get("FEEDBACK_DIR", "/persistent/results")
REVIEWS_DIR = os.environ.get("REVIEWS_DIR", "/persistent/reviews")

COPR_RESULT_TEMPLATE = "https://download.copr.fedorainfracloud.org" + \
                       "/results/{0}/{1}/srpm-builds/{2:08}"
# logdetective server URL
SERVER_URL = os.environ.get("SERVER_URL", "http://127.0.0.1:8000")


class ProvidersEnum(StrEnum):
    packit = "packit"
    copr = "copr"
    koji = "koji"
    url = "url"
    container = "container"
    debug = "debug"
    upload = "upload"


class BuildIdTitleEnum(StrEnum):
    copr = "Copr build"
    koji = "Koji build"
    packit = "Packit build"
    url = "URL"
    container = "Container log"
    debug = "Debug output"
