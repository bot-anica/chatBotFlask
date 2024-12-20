"""chat and message tables

Revision ID: 960c79cdfd55
Revises: 4a309a228ff2
Create Date: 2024-10-25 02:54:32.598775

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '960c79cdfd55'
down_revision = '4a309a228ff2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('chat', schema=None) as batch_op:
        batch_op.drop_index('ix_chat_title')
        batch_op.create_index(batch_op.f('ix_chat_title'), ['title'], unique=False)

    with op.batch_alter_table('message', schema=None) as batch_op:
        batch_op.drop_index('ix_message_text')
        batch_op.create_index(batch_op.f('ix_message_text'), ['text'], unique=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('message', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_message_text'))
        batch_op.create_index('ix_message_text', ['text'], unique=1)

    with op.batch_alter_table('chat', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_chat_title'))
        batch_op.create_index('ix_chat_title', ['title'], unique=1)

    # ### end Alembic commands ###
