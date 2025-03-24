from motor.motor_asyncio import AsyncIOMotorClient

mongodbUrl = "mongodb://localhost:27017/"
client = AsyncIOMotorClient(mongodbUrl)

db = client["fastapidb"]
user_collection = db["users"]