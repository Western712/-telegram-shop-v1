from sqlalchemy.ext.asyncio import AsyncSession

from app.models.product import Product


class StockService:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def change_stock(self, product: Product, quantity: int) -> Product:
        product.stock += quantity
        await self.session.commit()
        await self.session.refresh(product)
        return product
