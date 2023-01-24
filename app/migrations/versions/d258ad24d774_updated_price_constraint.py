"""updated price constraint

Revision ID: d258ad24d774
Revises: fb703b5c1583
Create Date: 2023-01-24 10:59:43.480965

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd258ad24d774'
down_revision = 'fb703b5c1583'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('activities', schema=None) as batch_op:
        batch_op.drop_constraint('activities_price_key', type_='unique')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('activities', schema=None) as batch_op:
        batch_op.create_unique_constraint('activities_price_key', ['price'])

    # ### end Alembic commands ###
