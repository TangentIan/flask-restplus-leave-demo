"""empty message

Revision ID: 36e0bc3977fc
Revises: 06237af3925e
Create Date: 2017-03-27 08:13:55.051480

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '36e0bc3977fc'
down_revision = '06237af3925e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('leave_remaining', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'leave_remaining')
    # ### end Alembic commands ###
