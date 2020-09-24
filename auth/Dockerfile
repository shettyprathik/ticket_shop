FROM xteleon/common as common

FROM python:3.8.2
WORKDIR /app
RUN pip install pipenv
COPY ./Pipfile* ./
RUN pipenv install --ignore-pipfile --deploy
COPY ./ ./
COPY --from=common /app /app/common
CMD ["pipenv", "run", "python", "index.py" ]