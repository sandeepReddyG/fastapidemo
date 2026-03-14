from fastapi import APIRouter
from app.models.schemas import HealthCheckResponse
from app.services.health_service import get_health_status

router = APIRouter()

@router.get("/health", response_model=HealthCheckResponse, tags=["Health"])
async def health_check():
    """
    Health check endpoint to verify the application's status.

    Returns:
        HealthCheckResponse: The health status of the application.
    """
    # Example values for uptime and version
    uptime = 123456  # This should be dynamically calculated
    version = "1.0.0"  # This should be fetched from application settings

    return get_health_status(uptime=uptime, version=version)