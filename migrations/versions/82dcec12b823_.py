"""empty message

Revision ID: 82dcec12b823
Revises: 
Create Date: 2024-04-03 13:21:50.839073

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '82dcec12b823'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('movies',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=80), nullable=True),
    sa.Column('description', sa.String(length=256), nullable=True),
    sa.Column('poster', sa.String(length=80), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('movies')
    # ### end Alembic commands ###
