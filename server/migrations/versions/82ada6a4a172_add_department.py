"""add Department

Revision ID: 82ada6a4a172
Revises: 5cb464acbd04
Create Date: 2024-04-11 20:51:05.559481

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '82ada6a4a172'
down_revision = '5cb464acbd04'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('department',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('address', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('department')
    # ### end Alembic commands ###
