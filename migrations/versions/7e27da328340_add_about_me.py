"""add about_me

Revision ID: 7e27da328340
Revises: 530001b0f99e
Create Date: 2017-10-11 14:40:45.013000

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7e27da328340'
down_revision = '530001b0f99e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('about_me', sa.Text(), nullable=True))
    op.add_column('users', sa.Column('gravatar_url', sa.String(length=128), nullable=True))
    op.add_column('users', sa.Column('nickname', sa.String(length=64), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'nickname')
    op.drop_column('users', 'gravatar_url')
    op.drop_column('users', 'about_me')
    # ### end Alembic commands ###