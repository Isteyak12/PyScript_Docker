# Use an official Python runtime as a base image
FROM python:3.9

# Set the working directory in the container
WORKDIR /app

# Copy the Python script and any other necessary files into the container
COPY BST.py /app/BST.py

# Install any dependencies required by your Python script
# If you have a requirements.txt file, uncomment the next line
# COPY requirements.txt /app/requirements.txt
# RUN pip install --no-cache-dir -r requirements.txt

# Expose the port (if your script runs a server or API)
# EXPOSE 8080

# Define the command to run your Python script
CMD ["python", "BST.py"]
