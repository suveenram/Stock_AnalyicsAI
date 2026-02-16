from pydantic import BaseModel


class Settings(BaseModel):
    app_name: str = "Stock Analytics AI"
    api_prefix: str = "/api/v1"
    disclaimer: str = "Educational only, not investment advice."
    provider_mode: str = "mock"


settings = Settings()
