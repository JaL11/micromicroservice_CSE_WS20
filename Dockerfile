# Pull base image
FROM python:3

# Set environment variables
##ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
RUN mkdir /chatbotservice
WORKDIR /chatbotservice

# Install dependencies
COPY requirements.txt /chatbotservice/
RUN pip install -r requirements.txt

#Copy project
COPY . /chatbot/
ENTRYPOINT ["python", "/chatbotservice/chatbot_server.py"]