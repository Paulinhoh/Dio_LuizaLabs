from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, ForeignKey, text

engine = create_engine('sqlite:///:memory:')
# Schema é o nome do banco de dados (eu acho)

metadata_obj = MetaData()
user = Table(
    'user',
    metadata_obj,
    Column('user_id', Integer, primary_key=True),
    Column('name', String(40), nullable=False),
    Column('email_address', String(60)),
    Column('nickname', String(50), nullable=False),
)

user_prefs = Table(
    'user_prefs',
    metadata_obj,
    Column('pref_id', Integer, primary_key=True),
    Column('pref_name', String(40), nullable=False),
    Column('pref_value', String(100)),
    Column('user_id', Integer, ForeignKey('user.user_id'), nullable=False)
)

for table in metadata_obj.sorted_tables:
    print(table)

print('\nInfo da tabela user_prefs')
print(user_prefs.primary_key)
print(user_prefs.constraints)

metadata_obj.create_all(engine)

metadata_db_obj = MetaData(schema='bank')
financial_info = Table(
    'financial_info',
    metadata_db_obj,
    Column('financial_id', Integer, primary_key=True),
    Column('financial_value', String(100), nullable=False),
)

print('\nInfo da tabela financial_info')
print(financial_info.primary_key)
print(financial_info.constraints)

# Estabelecendo conexão
connection = engine.connect()


sql_insert = text("INSERT INTO user VALUES (2, 'Maria', 'mari@gmail.com', 'Mari')")
connection.execute(sql_insert)

print('\nExecutando statement sql')
sql = text('SELECT * FROM user')
result = connection.execute(sql)
for row in result:
    print(row)
