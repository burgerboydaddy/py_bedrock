# AWS Bedrock Python Application

This project demonstrates how to connect to AWS Bedrock and send a message to an LLM model using Python and boto3.

## Prerequisites

- Docker and Docker Compose installed
- AWS account with Bedrock access
- AWS credentials (Access Key ID and Secret Access Key)

## Setup

1. Copy the example environment file and fill in your AWS credentials:

   ```bash
   cp .env.example .env
   ```

2. Edit the `.env` file with your actual AWS credentials:
   - `AWS_ACCESS_KEY_ID`: Your AWS Access Key ID
   - `AWS_ACCESS_KEY_SECRET`: Your AWS Secret Access Key
   - `AWS_REGION`: AWS region where Bedrock is available (e.g., us-east-1)
   - `LLM_MODEL`: The Bedrock model ID you want to use

## Running the Application

Build and run the Docker container:

```bash
docker-compose up --build
```

The application will:

1. Connect to AWS Bedrock using your credentials
2. Send the question "Why is sky blue?" to the specified LLM model
3. Display the response from the model
4. Exit

## Project Structure

- `main.py`: Main application code that connects to Bedrock
- `requirements.txt`: Python dependencies
- `Dockerfile`: Container configuration
- `docker-compose.yml`: Docker Compose configuration with environment variables
- `.env.example`: Example environment variables file

## Notes

- The code is configured for Claude 3 models by default. If using a different model family, you may need to adjust the request body format in `main.py`.
- Make sure your AWS account has the necessary permissions to access Bedrock and the specific model you're using.
- Never commit your `.env` file with actual credentials to version control.
