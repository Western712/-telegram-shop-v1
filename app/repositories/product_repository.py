from sqlalchemy import or_, select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.product import Product


class ProductRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def get_all(self) -> list[Product]:
        result = await self.session.execute(select(Product))
        return list(result.scalars().all())

    async def get_by_id(self, product_id: int) -> Product | None:
        result = await self.session.execute(
            select(Product).where(Product.id == product_id)
        )
        return result.scalar_one_or_none()

    async def get_by_article(self, article: str) -> Product | None:
        result = await self.session.execute(
            select(Product).where(Product.article == article)
        )
        return result.scalar_one_or_none()

    async def search(self, query: str) -> list[Product]:
        value = f"%{query}%"

        result = await self.session.execute(
            select(Product)
            .where(Product.status != "archived")
            .where(
                or_(
                    Product.name.ilike(value),
                    Product.brand.ilike(value),
                    Product.article.ilike(value),
                    Product.category.ilike(value),
                )
            )
            .limit(50)
        )

        return list(result.scalars().all())

    async def create(self, product: Product) -> Product:
        self.session.add(product)
        await self.session.commit()
        await self.session.refresh(product)
        return product
