"""add content column

Revision ID: 97cf242dcf4e
Revises: bc83cf556ec5
Create Date: 2022-07-25 11:13:23.738493

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '97cf242dcf4e'
down_revision = 'bc83cf556ec5'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('posts', 'content')
    pass
