FROM python:3.10
WORKDIR /home

COPY requirements.txt ./
RUN pip3 install --no-cache-dir -r requirements.txt

COPY server.py ./
CMD ["uvicorn", "server:app", "--host", "0.0.0.0", "--port", "8000"]
