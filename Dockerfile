# Use an official Python runtime as a parent image
FROM python:3.12-slim

# Set the working directory in the container
WORKDIR /usr/src/app

# Update apt-get and install build-essential and ffmpeg
RUN apt-get update && apt-get install -y \
    build-essential

# Install any needed packages specified in requirements.txt
COPY requirements.txt /usr/src/app
RUN pip install --no-cache-dir -r requirements.txt

# Copy the current directory contents into the container at /usr/src/app
COPY . /usr/src/app
COPY ./logo.png /usr/local/lib/python3.12/site-packages/streamlit/static/favicon.png

# Update the index
RUN python update_index.py

# Make port 8501 available to the world outside this container
EXPOSE 8501

# Run app.py when the container launches
CMD ["streamlit", "run", "app.py"]
