import json
import boto3
from botocore.exceptions import ClientError
from config import Config


def main():
    # Load configuration
    config = Config()
    
    print(f"Connecting to AWS Bedrock in region: {config.aws_region}")
    print(f"Using model: {config.llm_model}")
    
    # Create Bedrock client
    bedrock_runtime = boto3.client(
        service_name='bedrock-runtime',
        region_name=config.aws_region,
        aws_access_key_id=config.aws_access_key_id,
        aws_secret_access_key=config.aws_secret_access_key
    )
    
    # Prepare the message
    question = "Why is sky blue?"
    print(f"\nSending question: {question}\n")
    
    # Prepare request body (format depends on the model)
    # This example uses Claude 3 format, adjust based on your LLM_MODEL
    request_body = {
        "anthropic_version": "bedrock-2023-05-31",
        "max_tokens": 1000,
        "messages": [
            {
                "role": "user",
                "content": question
            }
        ]
    }
    
    try:
        # Invoke the model
        response = bedrock_runtime.invoke_model(
            modelId=config.llm_model,
            body=json.dumps(request_body)
        )
        
        # Parse response
        response_body = json.loads(response['body'].read())
        
        # Extract and print the answer
        if 'content' in response_body:
            # Claude 3 format
            answer = response_body['content'][0]['text']
        elif 'completion' in response_body:
            # Claude 2 format
            answer = response_body['completion']
        else:
            answer = json.dumps(response_body, indent=2)
        
        print("Response from Bedrock:")
        print("-" * 80)
        print(answer)
        print("-" * 80)
        
    except ClientError as e:
        print(f"Error calling Bedrock: {e}")
        raise
    except Exception as e:
        print(f"Unexpected error: {e}")
        raise


if __name__ == "__main__":
    main()
