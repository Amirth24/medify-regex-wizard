FROM python:3.12-alpine

ARG GEMINI_API_KEY
ENV GEMINI_API_KEY=$GEMINI_API_KEY

# Set the working directory
WORKDIR /app

COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000
ENV PORT=8000
ENV HOST=0.0.0.0


# Run the application
CMD ["python", "main.py"]
