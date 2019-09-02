"""empty message

Revision ID: 923efcde0236
Revises: 
Create Date: 2019-08-26 20:39:56.554759

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '923efcde0236'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Category',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(length=30), nullable=True),
    sa.Column('alias', sa.String(length=30), nullable=True),
    sa.Column('fid', sa.Integer(), nullable=True),
    sa.Column('keywords', sa.String(length=50), nullable=True),
    sa.Column('describe', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('alias'),
    sa.UniqueConstraint('name')
    )
    op.create_table('Article',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('title', sa.String(length=50), nullable=True),
    sa.Column('content', sa.Text(), nullable=True),
    sa.Column('titlepic', sa.String(length=50), nullable=True),
    sa.Column('describe', sa.Text(), nullable=True),
    sa.Column('keywords', sa.String(length=50), nullable=True),
    sa.Column('tags', sa.String(length=30), nullable=True),
    sa.Column('categoryid', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['categoryid'], ['Category.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('title')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('Article')
    op.drop_table('Category')
    # ### end Alembic commands ###
