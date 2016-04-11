"""empty message

Revision ID: 565623e10240
Revises: None
Create Date: 2016-04-10 23:36:45.614858

"""

# revision identifiers, used by Alembic.
revision = '565623e10240'
down_revision = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('contacts',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('first_name', sa.String(length=80), nullable=True),
    sa.Column('last_name', sa.String(length=80), nullable=True),
    sa.Column('job_title', sa.String(length=120), nullable=True),
    sa.Column('company', sa.String(length=120), nullable=True),
    sa.Column('phone_number', sa.String(length=120), nullable=True),
    sa.Column('email', sa.String(length=120), nullable=True),
    sa.Column('address1', sa.String(length=250), nullable=True),
    sa.Column('city', sa.String(length=120), nullable=True),
    sa.Column('state', sa.String(length=80), nullable=True),
    sa.Column('zipcode', sa.String(length=120), nullable=True),
    sa.Column('comments', sa.Text(), nullable=True),
    sa.Column('active_status', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('contacts')
    ### end Alembic commands ###