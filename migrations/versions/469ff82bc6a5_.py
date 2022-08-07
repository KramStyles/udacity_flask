"""empty message

Revision ID: 469ff82bc6a5
Revises: 
Create Date: 2022-08-07 10:26:03.143756

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '469ff82bc6a5'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('todos', sa.Column('completed', sa.Boolean(), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('todos', 'completed')
    # ### end Alembic commands ###
