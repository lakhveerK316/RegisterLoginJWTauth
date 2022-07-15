# from fastapi import (BackgroundTasks, UploadFile, 
#                     File, Form, Depends, HTTPException, status)

# from dotenv import dotenv_values
# from pydantic import BaseModel, EmailStr
# from typing import List
# from fastapi_mail import FastMail,ConnectionConfig, MessageSchema
# import jwt
# from main import templates
# from .models import User

# config_credentials = dict(dotenv_values(".env"))
# conf = ConnectionConfig(
#     MAIL_USERNAME = config_credentials["EMAIL"],
#     MAIL_PASSWORD = config_credentials["PASS"],
#     MAIL_FROM = config_credentials["EMAIL"],
#     MAIL_PORT = 587,
#     MAIL_SERVER = "smtp.gmail.com",
#     MAIL_TLS = True,
#     MAIL_SSL = False,
#     USE_CREDENTIALS = True
# )


# async def send_email(email : list, instance: User):

#     token_data = {
#         "id" : instance.id,
#         "username" : instance.username
#     }

#     token = jwt.encode(token_data, config_credentials["SECRET"])

#     message = MessageSchema(
#         subject=" Account Verification Mail",
#         recipients=email,  
#         # body=template,
#         subtype="html"
#         )

#     fm = FastMail(conf)
#     await fm.send_message(message) 