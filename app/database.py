import logging
from motor.motor_asyncio import AsyncIOMotorClient

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

mongodb_url = "mongodb://localhost:27017/"

try:
    client = AsyncIOMotorClient(mongodb_url)
    db = client["fastapidb"]
    user_collection = db["users"]

    logger.info("🚀 Successfully connected to MongoDB")
except Exception as e:
    logger.error(f"❌ Failed to connect to MongoDB: {e}")
