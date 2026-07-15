from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.product import Product


class ProductRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def get_all(self) -> list[Product]:
        result = await self.session.execute(select(Product))
        return list(result.scalars().all())

    async def get_by_article(self, article: str) -> Product | None:
        result = await self.session.execute(
            select(Product).where(Product.article == article)
        )
        return result.scalar_one_or_none()

    async def create(self, product: Product) -> Product:
        self.session.add(product)
        await self.session.commit()
        await self.session.refresh(product)
        return product
