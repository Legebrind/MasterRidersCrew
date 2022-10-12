"""empty message

Revision ID: 21371ff68c6f
Revises: 244835a17c16
Create Date: 2022-10-11 19:53:37.403108

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '21371ff68c6f'
down_revision = '244835a17c16'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('event', 'date',
               existing_type=sa.DATE(),
               type_=sa.DateTime(),
               existing_nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('event', 'date',
               existing_type=sa.DateTime(),
               type_=sa.DATE(),
               existing_nullable=False)
    # ### end Alembic commands ###
