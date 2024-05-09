#!/usr/bin/env python3
"""Example"""
from pymongo import MongoClient


client = MongoClient('mongodb://127.0.0.1:27017')
nginx = client.logs.nginx
find = {"method": "GET", "path": "/status"}
print(f"{nginx.count_documents({})} logs")
print("Methods:")
print(f'\tmethod GET: {nginx.count_documents({"method": "GET"})}')
print(f'\tmethod POST: {nginx.count_documents({"method": "POST"})}')
print(f'\tmethod PUT: {nginx.count_documents({"method": "PUT"})}')
print(f'\tmethod PATCH: {nginx.count_documents({"method": "PATCH"})}')
print(f'\tmethod DELETE: {nginx.count_documents({"method": "DELETE"})}')
print(f'{nginx.count_documents(find)} status check')
