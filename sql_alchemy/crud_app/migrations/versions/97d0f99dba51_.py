"""empty message

Revision ID: 97d0f99dba51
Revises: 3985d631658d
Create Date: 2020-05-16 00:50:38.666044

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '97d0f99dba51'
down_revision = '3985d631658d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('todo', sa.Column('completed', sa.Boolean(), nullable=True))
    op.execute('UPDATE todo SET completed = False WHERE completed IS NULL;')
    op.alter_column('todo', 'completed', nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('todo', 'completed')
    # ### end Alembic commands ###