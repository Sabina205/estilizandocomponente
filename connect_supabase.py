from supabase import Client, create_client

def get_connect_supabase():
    url = 'https://iehjnobslmqkzdulqoub.supabase.co'
    api_key = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImllaGpub2JzbG1xa3pkdWxxb3ViIiwicm9sZSI6ImFub24iLCJpYXQiOjE3MzQwOTQxNDIsImV4cCI6MjA0OTY3MDE0Mn0.cJSggR-1KV8pD1c12ar12GUjsCD_9TvWZZqia7Go7aU'

    supabase = create_client(url, api_key)
    return supabase