# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory to /app
WORKDIR /workspace

# Copy the requirements.txt and install dependencies
COPY requirements.txt /workspace/
RUN pip install -r requirements.txt

# Copy the FastAPI app file and the models folder
COPY app.py /workspace/
COPY models /models

# Expose port 80
EXPOSE 80

# Command to run the application
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "80"]