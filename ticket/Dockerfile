FROM xteleon/common:0.0.5 as common

FROM python:3.8.2
WORKDIR /app
RUN pip install pipenv
COPY ./Pipfile* ./
RUN pipenv install --ignore-pipfile --deploy
COPY ./ ./
COPY --from=common /app /app/common
CMD ["/bin/bash", "-c", "pipenv run gunicorn index:app -b 0.0.0.0:6000 --daemon && pipenv run python consume_broker.py"]
