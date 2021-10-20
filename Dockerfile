FROM python:3.8-slim-buster

# Make a Dir for our application
WORKDIR /app

# Install requirments
COPY requirements.txt .
RUN pip3 install -r requirements.txt

# Copy our source code
COPY . .

# Run the application
CMD ["python", "main.py"]