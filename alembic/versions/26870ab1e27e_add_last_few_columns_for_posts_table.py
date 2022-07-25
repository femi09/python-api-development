"""add last few columns for posts table

Revision ID: 26870ab1e27e
Revises: db82b2aa5185
Create Date: 2022-07-25 13:44:06.294945

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '26870ab1e27e'
down_revision = 'db82b2aa5185'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('published', sa.Boolean(), nullable=False, server_default='TRUE'))
    op.add_column('posts', sa.Column(
        'created_at', sa.TIMESTAMP(timezone=True), nullable=False, server_default=sa.text('Now()')))
    pass


def downgrade() -> None:
    op.drop_column("posts", "published"),
    op.drop_column("posts", "created_at")
    pass
