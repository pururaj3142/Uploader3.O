CP_TOKEN = os.environ.get("CP_TOKEN", "eyJhbGciOiJIUzM4NCIsInR5cCI6IkpXVCJ9.eyJpZCI6OTE4OTc2MTQsIm9yZ0lkIjozNDQ3NzcsInR5cGUiOjEsIm1vYmlsZSI6IjkxODczOTkyMTI5NyIsIm5hbWUiOiJQdXJ1cmFqIE1veWFsIiwiZW1haWwiOiI5MWI4M2FhNjU3NjE0ZGJmYjNkYjQ1OWRmMTk2MTI1YUBnbWFpbC5jb20iLCJpc0ZpcnN0TG9naW4iOnRydWUsImRlZmF1bHRMYW5ndWFnZSI6IkVOIiwiY291bnRyeUNvZGUiOiJJTiIsImlzSW50ZXJuYXRpb25hbCI6MCwiaXNEaXkiOnRydWUsImxvZ2luVmlhIjoiT3RwIiwiZmluZ2VycHJpbnRJZCI6IjU5NGYxOWQwMDdhZjQzODk5ZTQ3MjcxNjZkZmZkZTExIiwiaWF0IjoxNzY0MjA5OTExLCJleHAiOjE3NjQ4MTQ3MTF9.WC4Agl_1SfrUREPIfp2HBHw_kA74TExeXGzRW6BWBfOpLrj9eBBSjsMJ3cEHAULq")#🇳‌🇮‌🇰‌🇭‌🇮‌🇱‌
# Add your details here and then deploy by clicking on HEROKU Deploy button
import os
from os import environ

API_ID = int(environ.get("API_ID", "22049628"))
API_HASH = environ.get("API_HASH", "db9c4ee4be741f296522a9bb9a945722")
BOT_TOKEN = environ.get("BOT_TOKEN", "7615038215:AAHa3O-tVEfZHE_1p9sD0kLpIPVGEryTgD8")

OWNER = int(environ.get("OWNER", "670897324"))
CREDIT = environ.get("CREDIT", "DP 𝘽𝙊𝙏𝙎")
cookies_file_path = os.getenv("cookies_file_path", "youtube_cookies.txt")

TOTAL_USER = os.environ.get('TOTAL_USERS', '670897324').split(',')
TOTAL_USERS = [int(user_id) for user_id in TOTAL_USER]

AUTH_USER = os.environ.get('AUTH_USERS', '670897324').split(',')
AUTH_USERS = [int(user_id) for user_id in AUTH_USER]
if int(OWNER) not in AUTH_USERS:
    AUTH_USERS.append(int(OWNER))

# .....,.....,.......,...,.......,....., .....,.....,.......,...,.......,.....,
api_url = "http://master-api-v3.vercel.app/"
api_token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoiNzkxOTMzNDE5NSIsInRnX3VzZXJuYW1lIjoi4p61IFtvZmZsaW5lXSIsImlhdCI6MTczODY5MjA3N30.SXzZ1MZcvMp5sGESj0hBKSghhxJ3k1GTWoBUbivUe1I"
# .....,.....,.......,...,.......,....., .....,.....,.......,...,.

