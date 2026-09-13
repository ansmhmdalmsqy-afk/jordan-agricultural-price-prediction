import os
import ee
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

project_id = os.getenv("GEE_PROJECT_ID")

print(f"🔍 Loaded Project ID from .env: '{project_id}'")

if not project_id:
    raise ValueError("❌ GEE_PROJECT_ID is not defined in .env file!")

try:
    # Initialize GEE with explicitly configured Google Cloud Project ID
    ee.Initialize(project=project_id)
    print(
        f"✅ Successfully initialized Google Earth Engine with project: '{project_id}'"
    )

    # Validate data retrieval: Fetch Sentinel-2 imagery over Jordan Valley
    jordan_valley = ee.Geometry.Point([35.5, 32.0])
    collection = (
        ee.ImageCollection("COPERNICUS/S2_SR_HARMONIZED")
        .filterBounds(jordan_valley)
        .filterDate("2024-01-01", "2024-01-31")
    )

    image_count = collection.size().getInfo()
    print(
        f"🛰️ Pipeline Validated: Fetched {image_count} Sentinel-2 images over Jordan Valley for Jan 2024."
    )

except Exception as e:
    print(f"❌ Connection error: {e}")