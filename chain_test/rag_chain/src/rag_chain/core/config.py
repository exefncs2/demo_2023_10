from dotenv import load_dotenv
import os

class Settings:
    def __init__(self):
        load_dotenv()  # Load environment variables from .env file

        self.database_uri = os.getenv("DATABASE_URI")
        self.openai_api_key = os.getenv("OPENAI_API_KEY")
        self.gcp_project_id = os.getenv("GCP_PROJECT_ID")
        self.gcp_project_secret_name = os.getenv("GCP_PROJECT_SECTET_NAME")
        self.google_application_credentials = os.getenv("GOOGLE_APPLICATION_CREDENTIALS")
        self.gpt_version = os.getenv("GPT_VERSION")

settings = Settings()

