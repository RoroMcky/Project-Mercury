"""empty message

Revision ID: 9221c3a12a21
Revises: 13df519645bb
Create Date: 2018-05-19 21:57:34.039463

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9221c3a12a21'
down_revision = '13df519645bb'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('firstname', sa.String(length=255), nullable=True))
    op.add_column('user', sa.Column('lastname', sa.String(length=255), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'lastname')
    op.drop_column('user', 'firstname')
    # ### end Alembic commands ###