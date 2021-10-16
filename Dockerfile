FROM python:3.9-slim-buster
# Make a Dir for our application
WORKDIR /app

# Install requirments
COPY app/requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

# Copy our source code
COPY /app .

RUN  apt-get update && apt-get install -y wget

#Loading The Model
RUN wget https://abbyani.xyz/vFjXi.sav
RUN mkdir ./model
RUN mv ./vFjXi.sav ./model/vFjXi.sav

EXPOSE 8081

# Run the application
CMD [ "python", "main.py"]