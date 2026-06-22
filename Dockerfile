FROM python:3.12-slim
WORKDIR /repo
COPY . /repo
RUN python -B scripts/setup_repo.py
CMD ["make", "demo-light"]
