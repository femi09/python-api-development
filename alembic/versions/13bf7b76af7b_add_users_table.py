"""add users table

Revision ID: 13bf7b76af7b
Revises: 97cf242dcf4e
Create Date: 2022-07-25 11:18:35.046000

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '13bf7b76af7b'
down_revision = '97cf242dcf4e'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('users',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('email', sa.String(), nullable=False),
                    sa.Column('password', sa.String(), nullable=False),
                    sa.Column('created_at', sa.TIMESTAMP(timezone=True), server_default=sa.text(
                        'now()'), nullable=False), sa.PrimaryKeyConstraint('id'),
                    sa.UniqueConstraint('email, id')),
    pass


def downgrade() -> None:
    op.drop_table('users')
    pass
