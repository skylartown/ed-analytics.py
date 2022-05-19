from distutils.core import setup

from ed_analytics.consts import AUTHOR, AUTHOR_EMAIL, DESCRIPTION, LONG_DESCRIPTION, MAINTAINER, MAINTAINER_EMAIL, NAME, VERSION


setup(
    name=NAME,
    version=VERSION,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,

    maintainer=MAINTAINER,
    maintainer_email=MAINTAINER_EMAIL,

    url="https://github.com/skylartown/ed-analytics.py",

    license="MIT",
    keywords=[
        "education",
        "analytics",
        "classroom"
    ],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: Implementation :: CPython",
        "Intended Audience :: Education"
    ],
    package_dir=["ed_analytics"],
)
