from app import db,ma
## MODEL ######
from datetime import datetime

''' My Marshmallow '''
get_values = lambda m: list(map(lambda a: getattr(m,a), m.fields ))
model2dict = lambda m: dict(zip( m.fields,get_values(m) ))

def dict2model(row, data):
  for field in row.fields:
    if field in data:
      setattr(row, field, data[field])
  return row

class Base():
  def from_dict(self, data):
     return dict2model(self, data)

  @staticmethod
  def to_list(list_rows):
     return list(map(lambda m: m.to_dict(), list_rows))

  def to_dict(self):
    data = model2dict(self)
    return data


''' Data models '''
class Empleado(db.Model,Base):
  __tablename__ = 'empleados'
  fields = ('empleado_id','nombre','apellido')
  empleado_id = db.Column(db.Integer, primary_key=True)#autoincrement by default
  nombre = db.Column(db.String(40), nullable=False)
  apellido = db.Column(db.String(40), nullable=False)
  def __repr__(self):
    return '<Empleado {}, {}, {}>'.format(*get_values(self))


class Turno(db.Model,Base):
  __tablename__ = 'turnos'
  fields = ('t_id','h_entrada','h_salida','fecha','empleado_id')
  t_id = db.Column(db.Integer, primary_key=True)
  h_entrada = db.Column(db.String(5), nullable=False)
  h_salida = db.Column(db.String(5), nullable=False)
  fecha = db.Column(db.String(10), nullable=False)
  empleado_id = db.Column(db.Integer, db.ForeignKey('empleados.empleado_id')\
    ,nullable=False)
  empleado = db.relationship('Empleado',
      backref=db.backref('turnos', lazy=True))
  def __repr__(self):
      return '<Turno %r>' % self.t_id


''' Data schemas '''
class TurnoSchema(ma.Schema):
  class Meta:# serialize or jsonify
    fields = ('t_id','h_entrada','h_salida','fecha','empleado_id')


class EmpleadoSchema(ma.Schema):
  class Meta:
    fields = ('empleado_id','nombre','apellido')


###  Init schema
turno_schema  = TurnoSchema()
turnos_schema= TurnoSchema(many=True)

empleado_schema = EmpleadoSchema()
empleados_schema= EmpleadoSchema(many=True)