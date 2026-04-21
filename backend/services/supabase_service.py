from supabase import create_client, Client
from core.config import settings

# Initialize once here
supabase_url = settings.supabase_url
supabase_key = settings.supabase_service_role_key or settings.supabase_api_key

if not supabase_url or not supabase_key:
    raise RuntimeError("SUPABASE_URL and a Supabase API key must be configured")

# This is the actual live object you use to run .table().upsert()
supabase: Client = create_client(supabase_url, supabase_key)
