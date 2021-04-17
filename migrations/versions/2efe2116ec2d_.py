"""empty message

Revision ID: 2efe2116ec2d
Revises:
Create Date: 2021-04-17 09:26:53.036286

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2efe2116ec2d'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('characters', sa.Column('image_path', sa.String(length=255), nullable=False))
    op.add_column('characters', sa.Column('name', sa.String(length=255), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('characters', 'name')
    op.drop_column('characters', 'image_path')
    # ### end Alembic commands ###
