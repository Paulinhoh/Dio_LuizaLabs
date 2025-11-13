from sqlalchemy import Column, Integer, String, ForeignKey, create_engine, inspect, select, func
from sqlalchemy.orm import declarative_base, relationship, Session

base = declarative_base()


class User(base):
    __tablename__ = 'user_account'

    # Atributos
    id = Column(Integer, primary_key=True)
    name = Column(String)
    fullname = Column(String)

    # Relação entre as tabelas
    address = relationship(
        "Address", back_populates="user", cascade="all, delete-orphan"
    )

    def __repr__(self):
        return f"User (id={self.id}, name={self.name}, fullname={self.fullname})"


class Address(base):
    __tablename__ = 'address'

    id = Column(Integer, primary_key=True, autoincrement=True)
    email_address = Column(String(30), nullable=False, unique=True)
    user_id = Column(Integer, ForeignKey('user_account.id'), nullable=False)

    user = relationship(
        "User", back_populates="address"
    )

    def __repr__(self):
        return f"Address (id={self.id}, email_address={self.email_address})"


print(User.__tablename__)
print(Address.__tablename__)

# Conexão com o banco de dados
engine = create_engine('sqlite://')

# Criando as classes como tabelas no banco de dados
base.metadata.create_all(engine)

# Verificando se a tabela user_account existe
inspector_engine = inspect(engine)
print(inspector_engine.has_table('user_account'))

# Retorna os nomes de todas as tabelas
print(inspector_engine.get_table_names())

# Retorna o nome do Schema
print(inspector_engine.default_schema_name)

# Fazendo a inserção de dados no banco, caso algo de errado esse campo with garante o rollback do banco
with Session(engine) as session:
    juliana = User(
        name='Juliana',
        fullname='Juliana Santos',
        address=[Address(email_address='julianasantos@gmail.com')]
    )

    sandy = User(
        name='Sandy',
        fullname='Sandy Silva',
        address=[
            Address(email_address='sandy@gmail.com'),
            Address(email_address='sandy2@gmail.com')
        ]
    )

    patrick = User(
        name='Patrick',
        fullname='Patrick Reis'
    )

    # enviando para o BD (persistência de dados)
    session.add_all([juliana, sandy, patrick])
    session.commit()

print('\nRecuperando usuários a partir de condições de filtragem')
stmt_users = select(User).where(User.name.in_(['Juliana']))  # stmt == statement
for user in session.scalars(stmt_users):
    print(user)

print('\nRecuperando os endereços de e-mail de Sandy')
stmt_address = select(Address.email_address).where(Address.user_id.in_([2]))
for address in session.scalars(stmt_address):
    print(address)

print('\nRecuperando os Users de maneira ordenada')
stmt_order = select(User).order_by(User.fullname.desc())
for result in session.scalars(stmt_order):
    print(result)

print('\nRecuperando os dados usando join')
stmt_join = select(User.fullname, Address.email_address).join_from(Address, User)
for result in session.scalars(stmt_join):
    print(result)

print(stmt_join)

print('\nExecutando statement a partir da connection')
connection = engine.connect()
result = connection.execute(stmt_join).fetchall()
print(result)

print('\nTotal de instancias em Users')
stmt_count = select(func.count('*')).select_from(User)
for result in session.scalars(stmt_count):
    print(result)
