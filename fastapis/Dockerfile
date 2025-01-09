# Use the official Python image from the Docker Hub
FROM python:3.12-slim

# Set the working directory in the container
WORKDIR /code

# Copy the dependencies file to the working directory
COPY ./requirements.txt /code/requirements.txt

# Install dependencies 
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# Copy the code from the host to the container
COPY ./app /code/app

# Command to run the FastAPI app using uvicorn
CMD ["fastapi", "run", "app/main.py", "--port", "80"]