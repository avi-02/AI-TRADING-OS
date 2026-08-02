from fastapi import APIRouter, HTTPException

from app.models.overview import MarketOverview
from app.services.overview_service import get_market_overview

router = APIRouter(
    prefix="/market",
    tags=["Market Overview"]
)


@router.get(
    "/overview",
    response_model=MarketOverview
)
def market_overview():
    """
    Return a high-level overview of the tracked market.
    """
    try:
        return get_market_overview()

    except ValueError as e:
        raise HTTPException(
            status_code=404,
            detail=str(e)
        )