FROM python:3.8
WORKDIR /workdir
COPY . .
RUN pip install \
    black \
    codecov \
    flake8 \
    mutmut \
    pandas \
    pylint \
    pytest \
    pytest-cov \
    pytest-mock \
    rope \
    typer
CMD make
