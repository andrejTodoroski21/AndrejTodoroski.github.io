"""empty message

Revision ID: a129beaacccf
Revises: 
Create Date: 2024-05-30 13:34:23.960543

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a129beaacccf'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users_table',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('first_name', sa.String(), nullable=False),
    sa.Column('last_name', sa.String(), nullable=False),
    sa.Column('username', sa.String(), nullable=False),
    sa.Column('_hashed_password', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('username')
    )
    op.create_table('items_table',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('item_name', sa.String(), nullable=False),
    sa.Column('item_img', sa.String(), nullable=False),
    sa.Column('category', sa.String(), nullable=False),
    sa.Column('description', sa.String(), nullable=True),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('(CURRENT_TIMESTAMP)'), nullable=True),
    sa.Column('price', sa.Integer(), nullable=False),
    sa.Column('inventory', sa.Integer(), nullable=False),
    sa.Column('seller_id', sa.Integer(), nullable=True),
    sa.Column('buyer_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['buyer_id'], ['users_table.id'], name=op.f('fk_items_table_buyer_id_users_table')),
    sa.ForeignKeyConstraint(['seller_id'], ['users_table.id'], name=op.f('fk_items_table_seller_id_users_table')),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('carts_table',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('price_sold', sa.Integer(), nullable=False),
    sa.Column('item_id', sa.Integer(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('sold_at', sa.DateTime(), server_default=sa.text('(CURRENT_TIMESTAMP)'), nullable=True),
    sa.ForeignKeyConstraint(['item_id'], ['items_table.id'], name=op.f('fk_carts_table_item_id_items_table')),
    sa.ForeignKeyConstraint(['user_id'], ['users_table.id'], name=op.f('fk_carts_table_user_id_users_table')),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('comments_table',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('content', sa.String(), nullable=False),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('(CURRENT_TIMESTAMP)'), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('item_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['item_id'], ['items_table.id'], name=op.f('fk_comments_table_item_id_items_table')),
    sa.ForeignKeyConstraint(['user_id'], ['users_table.id'], name=op.f('fk_comments_table_user_id_users_table')),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('comments_table')
    op.drop_table('carts_table')
    op.drop_table('items_table')
    op.drop_table('users_table')
    # ### end Alembic commands ###
