from fastapi import APIRouter

from app.api.items import router as items_router

router = APIRouter(prefix="/api")
router.include_router(items_router)
