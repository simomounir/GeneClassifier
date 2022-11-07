FROM python:3.10.8
LABEL maitainer="mounir.mohammed92@gmail.com"

# install build utilities
RUN apt-get update && \
	apt-get install -y gcc make apt-transport-https ca-certificates build-essential

# check our python environment
RUN python3 --version
RUN pip3 --version

# set the working directory for containers
WORKDIR  /usr/src/GeneClassifier

# Installing python dependencies
RUN pip install --no-cache-dir git+https:https://github.com/simomounir/GeneClassifier.git

# Copy all the files from the project’s root to the working directory
COPY example.py example.py
RUN ls -la /*

# Running Python Application
CMD ["python3", "example.py"]