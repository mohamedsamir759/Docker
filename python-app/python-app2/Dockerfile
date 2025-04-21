
FROM python:3.11-slim
WORKDIR /python-app
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
LABEL website="geeksforgeeks"
EXPOSE 5000
CMD ["python", "app.py"]
