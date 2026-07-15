from alembic import op
import sqlalchemy as sa

revision = "0001_initial"
down_revision = None


def upgrade():
    op.create_table(
        "categories",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column("name", sa.String(length=100), unique=True),
    )

    op.create_table(
        "admins",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column("telegram_id", sa.BigInteger(), unique=True),
        sa.Column("name", sa.String(length=255)),
        sa.Column("role", sa.String(length=50)),
        sa.Column("is_active", sa.Boolean()),
    )

    op.create_table(
        "products",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column("article", sa.String(length=100), unique=True),
        sa.Column("name", sa.String(length=255)),
        sa.Column("brand", sa.String(length=100)),
        sa.Column("category", sa.String(length=100)),
        sa.Column("price", sa.Numeric(10, 2)),
        sa.Column("stock", sa.Integer()),
        sa.Column("status", sa.String(length=50)),
    )


def downgrade():
    op.drop_table("products")
    op.drop_table("admins")
    op.drop_table("categories")
