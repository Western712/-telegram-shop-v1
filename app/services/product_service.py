from sqlalchemy.ext.asyncio import AsyncSession

from app.models.product import Product
from app.repositories.product_repository import ProductRepository


class ProductService:
    def __init__(self, session: AsyncSession):
        self.repository = ProductRepository(session)

    async def create_product(self, **data) -> Product:
        product = Product(**data)
        return await self.repository.create(product)

    async def get_products(self) -> list[Product]:
        return await self.repository.get_all()

    async def get_product_by_article(self, article: str) -> Product | None:
        return await self.repository.get_by_article(article)

    async def get_product(self, product_id: int) -> Product | None:
        return await self.repository.get_by_id(product_id)

    async def search(self, query: str) -> list[Product]:
        return await self.repository.search(query)
