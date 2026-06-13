import enum

from sqlalchemy import BigInteger, CheckConstraint, Column, Date, Enum, MetaData, String, Table, Text, Time, text

metadata = MetaData()


class Service(str, enum.Enum):
    КОНСУЛЬТАЦИЯ = 'Консультация'
    ЛЕЧЕНИЕ = 'Лечение'
    ПРОТЕЗИРОВАНИЕ = 'Протезирование'
    ЧИСТКА = 'Чистка'


t_apps = Table(
    'apps', metadata,
    Column('fio', String(255)),
    Column('phone', BigInteger),
    Column('service_list', Enum(Service, values_callable=lambda cls: [member.value for member in cls], name='service')),
    Column('my_data', Date, server_default=text('CURRENT_DATE')),
    Column('my_time', Time, server_default=text('CURRENT_TIME')),
    Column('problem', Text),
    CheckConstraint('length(fio::text) >= 5', name='apps_fio_check'),
    CheckConstraint("phone = '70000000000'::bigint AND phone <= '89999999999'::bigint", name='apps_phone_check')
)
