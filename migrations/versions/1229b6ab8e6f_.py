"""empty message

Revision ID: 1229b6ab8e6f
Revises: 
Create Date: 2022-11-09 17:37:26.772427

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1229b6ab8e6f'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(length=120), nullable=False),
    sa.Column('password', sa.String(length=80), nullable=False),
    sa.Column('is_active', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.create_table('event',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=120), nullable=False),
    sa.Column('start', sa.String(), nullable=False),
    sa.Column('end', sa.String(), nullable=False),
    sa.Column('map', sa.String(), nullable=False),
    sa.Column('owner_id', sa.Integer(), nullable=False),
    sa.Column('date', sa.String(), nullable=False),
    sa.Column('private', sa.Boolean(), nullable=True),
    sa.Column('slug', sa.String(), nullable=False),
    sa.Column('description', sa.String(), nullable=False),
    sa.Column('origin_lon', sa.Float(), nullable=False),
    sa.Column('origin_lat', sa.Float(), nullable=False),
    sa.Column('destination_lon', sa.Float(), nullable=False),
    sa.Column('destination_lat', sa.Float(), nullable=False),
    sa.Column('hours', sa.String(), nullable=False),
    sa.Column('minutes', sa.String(), nullable=False),
    sa.ForeignKeyConstraint(['owner_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('form_friendship',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('main_friend_id', sa.Integer(), nullable=False),
    sa.Column('secondary_friend_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['main_friend_id'], ['user.id'], ),
    sa.ForeignKeyConstraint(['secondary_friend_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('group',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=10), nullable=False),
    sa.Column('owner_id', sa.Integer(), nullable=False),
    sa.Column('private', sa.Boolean(), nullable=True),
    sa.ForeignKeyConstraint(['owner_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('image',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('image', sa.String(), nullable=False),
    sa.Column('owner_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['owner_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('event_participation',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('event_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['event_id'], ['event.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('group_participation',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('group_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['group_id'], ['group.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('post',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('text', sa.String(length=5000), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('image_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['image_id'], ['image.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user__data',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=120), nullable=False),
    sa.Column('last_name', sa.String(length=120), nullable=False),
    sa.Column('address', sa.String(length=120), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('profile_picture', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['profile_picture'], ['image.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user__data')
    op.drop_table('post')
    op.drop_table('group_participation')
    op.drop_table('event_participation')
    op.drop_table('image')
    op.drop_table('group')
    op.drop_table('form_friendship')
    op.drop_table('event')
    op.drop_table('user')
    # ### end Alembic commands ###
