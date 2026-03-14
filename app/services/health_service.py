from app.core.config import settings
from app.models.schemas import HealthCheckResponse

def get_health_status(uptime: int, version: str) -> HealthCheckResponse:
    """
    Returns the health status of the application.

    Args:
        uptime (int): The uptime of the application in seconds.
        version (str): The current version of the application.

    Returns:
        HealthCheckResponse: The health status response model.
    """
    return HealthCheckResponse(
        status="healthy",
        uptime=uptime,
        version=version
    )