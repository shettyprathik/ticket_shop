FROM xteleon/common:1.0.7 as common

FROM python:3.8.2
WORKDIR /app
RUN pip install pipenv
COPY ./Pipfile* ./
RUN pipenv install --ignore-pipfile --deploy
COPY ./ ./
COPY --from=common /app /app/common
CMD ["/bin/bash","-c", "pipenv run celery -A src worker -l INFO -D && pipenv run python index.py"]