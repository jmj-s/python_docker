# set base image (host os)
FROM python

# set the working directory in the container

WORKDIR /code

# Copy dependencies to the working directory
COPY requirements.txt . 

# Install dependencies
RUN pip install -r requirements.txt

# Copy the content of the local src directory to the working directory
COPY src/ . 

# command to run on container start
CMD ["python", "./app.py"]
