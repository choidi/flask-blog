"""Delete tags table

Revision ID: 351905d23764
Revises: 1f91eb77bf2e
Create Date: 2017-10-12 12:01:07.558000

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '351905d23764'
down_revision = '1f91eb77bf2e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('articles_tags')
    op.drop_table('tags')
    op.add_column('articles', sa.Column('tags', sa.String(length=64), nullable=True))
    op.create_index(op.f('ix_articles_create_timestramp'), 'articles', ['create_timestramp'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_articles_create_timestramp'), table_name='articles')
    op.drop_column('articles', 'tags')
    op.create_table('tags',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('name', sa.VARCHAR(length=50), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('articles_tags',
    sa.Column('tag_id', sa.INTEGER(), nullable=False),
    sa.Column('article_id', sa.INTEGER(), nullable=False),
    sa.ForeignKeyConstraint(['article_id'], [u'articles.id'], ),
    sa.ForeignKeyConstraint(['tag_id'], [u'tags.id'], ),
    sa.PrimaryKeyConstraint('tag_id', 'article_id')
    )
    # ### end Alembic commands ###
