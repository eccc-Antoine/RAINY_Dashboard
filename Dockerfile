# Use a lightweight official Python base image
FROM python:3.11-slim

# Set working directory inside the container
WORKDIR /app

# Copy requirements first (better caching)
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the repo (your Streamlit app)
COPY . .

# Expose Streamlit’s default port
EXPOSE 8501

# Run the Streamlit app
CMD ["streamlit", "run", "DASHBOARDS/ISEE/ISEE_DASH_LIGHT_2.py", "--server.port=8501", "--server.address=0.0.0.0"]