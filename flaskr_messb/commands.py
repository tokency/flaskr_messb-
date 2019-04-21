import click

from flaskr_messb import app,db
from flaskr_messb.models import Message


@app.cli.command()
@click.option('--drop',is_flag=True,help='Create after drop.')
def initdb(drop):
	if drop:
		click.confirm('此操作是删除数据库，是否要继续？',abort=True)
		db.drop_all()
		click.echo('删除表')
	db.create_all()
	click.echo('初始化数据库')


@app.cli.command()
@click.option('--count',default=10,help='half')
def forge(count):
	from faker import Faker

	db.drop_all()
	db.create_all()

	fake = Faker()
	click.echo('working...')

	for i in range(count):
		message = Message(name=fake.name(),body=fake.sentence(),timestamp=fake.date_time_this_year())
		db.session.add(message)

	db.session.commit()
	click.echo('create %d fake messages.' % count)