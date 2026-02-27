from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

revision: str = "df8b0985be94"
down_revision: Union[str, Sequence[str], None] = "e87c7cf9183b"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.alter_column(
        "students",
        "created_at",
        existing_type=postgresql.TIMESTAMP(),
        server_default=sa.text("now()"),
        existing_nullable=False,
    )
    op.alter_column(
        "students",
        "updated_at",
        existing_type=postgresql.TIMESTAMP(),
        server_default=sa.text("now()"),
        existing_nullable=False,
    )


def downgrade() -> None:
    op.alter_column(
        "students",
        "updated_at",
        existing_type=postgresql.TIMESTAMP(),
        server_default=None,
        existing_nullable=False,
    )
    op.alter_column(
        "students",
        "created_at",
        existing_type=postgresql.TIMESTAMP(),
        server_default=None,
        existing_nullable=False,
    )