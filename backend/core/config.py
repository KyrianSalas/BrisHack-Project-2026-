from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    supabase_url: str
    supabase_api_key: str
    supabase_service_role_key: str | None = None
    cache_admin_token: str | None = None
    cors_allowed_origins: str | None = None

    model_config = SettingsConfigDict(env_file=".env")

settings = Settings()