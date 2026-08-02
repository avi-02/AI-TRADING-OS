from typing import List

from fastapi import APIRouter, Query

from app.models.market import MarketTicker
from app.services.scanner_service import (
    get_high_volume,
    get_most_active,
    get_top_gainers,
    get_top_losers,
)

router = APIRouter(
    prefix="/scanner",
    tags=["Market Scanner"],
)


@router.get(
    "/gainers",
    response_model=List[MarketTicker],
)
def top_gainers(
    limit: int = Query(
        default=5,
        ge=1,
        le=50,
        description="Number of top gaining assets",
    ),
):
    return get_top_gainers(limit)


@router.get(
    "/losers",
    response_model=List[MarketTicker],
)
def top_losers(
    limit: int = Query(
        default=5,
        ge=1,
        le=50,
        description="Number of top losing assets",
    ),
):
    return get_top_losers(limit)


@router.get(
    "/high-volume",
    response_model=List[MarketTicker],
)
def high_volume(
    limit: int = Query(
        default=5,
        ge=1,
        le=50,
        description="Assets ranked by quote volume",
    ),
):
    return get_high_volume(limit)


@router.get(
    "/most-active",
    response_model=List[MarketTicker],
)
def most_active(
    limit: int = Query(
        default=5,
        ge=1,
        le=50,
        description="Assets ranked by trade count",
    ),
):
    return get_most_active(limit)