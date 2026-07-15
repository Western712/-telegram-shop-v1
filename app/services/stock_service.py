from sqlalchemy.ext.asyncio import AsyncSession

from app.models.product import Product
from app.models.stock_movement import StockMovement


class StockService:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def change_stock(
        self,
        product: Product,
        quantity: int,
        admin_id: int | None = None,
        comment: str | None = None,
    ) -> Product:
        new_stock = product.stock + quantity

        if new_stock < 0:
            raise ValueError("Недостаточно товара на складе")

        old_stock = product.stock
        product.stock = new_stock

        movement = StockMovement(
            product_id=product.id,
            admin_id=admin_id,
            movement_type="income" if quantity > 0 else "expense",
            quantity=quantity,
            comment=comment,
        )

        self.session.add(movement)

        if product.stock == 0:
            product.status = "out_of_stock"
        else:
            product.status = "available"

        await self.session.commit()
        await self.session.refresh(product)
        return product
