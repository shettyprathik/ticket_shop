<<<<<<< HEAD
FROM xteleon/common as common
=======
FROM xteleon/common:0.0.5 as common
>>>>>>> 0156a6df5ae8697cbcd5345116f15d658e4a4c3e

FROM python:3.8.2
WORKDIR /app
RUN pip install pipenv
COPY ./Pipfile* ./
RUN pipenv install --ignore-pipfile --deploy
COPY ./ ./
COPY --from=common /app /app/common
<<<<<<< HEAD
CMD ["pipenv", "run", "python", "index.py" ]
=======
CMD ["pipenv", "run", "python", "index.py"]
>>>>>>> 0156a6df5ae8697cbcd5345116f15d658e4a4c3e
