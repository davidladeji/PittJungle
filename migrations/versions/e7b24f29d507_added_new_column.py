"""added new column

Revision ID: e7b24f29d507
Revises: 51f5ccfba190
Create Date: 2020-11-09 01:31:02.044932

"""

# revision identifiers, used by Alembic.
revision = 'e7b24f29d507'
down_revision = '51f5ccfba190'

from alembic import op
import sqlalchemy as sa


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('fastfood', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'fastfood')
    # ### end Alembic commands ###
