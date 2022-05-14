"""empty message

Revision ID: 85caf574ed00
Revises: 6832ec1b1b18
Create Date: 2022-05-10 19:15:00.438638

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '85caf574ed00'
down_revision = '6832ec1b1b18'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('data',
    sa.Column('pokemon_id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('hp', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('pokemon_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('data')
    # ### end Alembic commands ###