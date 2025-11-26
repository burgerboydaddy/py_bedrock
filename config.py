from pydantic_settings import BaseSettings
from pydantic import Field


class Config(BaseSettings):
    """Configuration class to manage environment variables using Pydantic"""
    
    aws_access_key_id: str = Field(..., alias='AWS_ACCESS_KEY_ID')
    aws_secret_access_key: str = Field(..., alias='AWS_ACCESS_KEY_SECRET')
    aws_region: str = Field(default='us-west-2', alias='AWS_REGION')
    llm_model: str = Field(..., alias='LLM_MODEL')
    
    class Config:
        env_file = '.env'
        env_file_encoding = 'utf-8'
        case_sensitive = True
        extra = 'ignore'  # Ignore extra environment variables not defined in model
