FROM python:3.8

RUN pip install virtualenv
ENV VIRTUAL_ENV=/venv
RUN virtualenv venv -p python3
ENV PATH="VIRTUAL_ENV/bin:$PATH"

WORKDIR /app
ADD . /app

# Install dependencies
RUN pip install -r requirements.txt

# Expose port 
EXPOSE 5000

# Run the application:
#####Enter the Command to run the app here. The line below is incomplete
#########Enter code here#################
CMD gunicorn -b 0.0.0.0:5000 --workers=2 app:app
