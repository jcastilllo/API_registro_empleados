from flask import Blueprint, jsonify, request, redirect, url_for

from app import db
from models import (Empleado, Turno,
  turno_schema, turnos_schema,
  empleado_schema, empleados_schema)

api = Blueprint('api', __name__)

from errors import bad_request, error_response

@api.route('/', methods=['GET'])
def home():
    return jsonify({'Hello':'World'})


#################  EMPLEADO #################
# Create
@api.route('/empleado/', methods=['POST'])
def add_empleado():
  data = request.get_json() or {}
  empl = Empleado().from_dict(data)
  db.session.add(empl)
  db.session.commit()
  response = jsonify(empl.to_dict())
  response.headers['Location'] = url_for('api.get_empleado',empleado_id=empl.empleado_id )
  return response, 201
# Read one
@api.route('/empleado/<int:empleado_id>', methods=['GET'])
def get_empleado(empleado_id):
  empl = Empleado.query.get_or_404(empleado_id)
  #return product_schema.jsonify(prod)
  return jsonify(empl.to_dict())

# Read many
@api.route('/empleado/', methods=['GET'])
def get_empleados():
  all_empleados = Empleado.query.all()
  #print(all_products)
  result = empleados_schema.dump(all_empleados)
  #return jsonify(result)
  return jsonify(Empleado.to_list(all_empleados))
# Update
@api.route('/empleado/<int:empleado_id>', methods=['PUT'])
def update_empleado(empleado_id):
  data = request.get_json() or {}
  empl = Empleado.query.get_or_404(empleado_id)
  empl.from_dict(data) # update
  #print(data,prod)
  db.session.commit()
  response = jsonify(empl.to_dict())
  response.headers['Location'] = url_for('api.get_empleado', empleado_id=empl.empleado_id)
  return response, 200
# Delete
@api.route('/empleado/<int:empleado_id>', methods=['DELETE'])
def del_empleado(empleado_id):
  empl = Empleado.query.get_or_404(empleado_id)
  db.session.delete(empl)
  db.session.commit()
  result = {'msg':'Empleado deleted',
       'Empleado':empl.to_dict() }
  response = jsonify(result)
  return response, 200
#################  turnos  #################
# Create
@api.route('/turno/', methods=['POST'])
def add_turno():
  data = request.get_json() or {}
  print ("###############  /turno/test77  POST ###########################")
  print (data)
  tur = Turno().from_dict(data)
  print (tur)
  db.session.add(tur)
  db.session.commit()
  response = jsonify(tur.to_dict())
  response.headers['Location'] = url_for('api.get_turno', t_id=tur.t_id)  
  return response, 201  
# Read one
@api.route('/turno/<int:t_id>', methods=['GET'])
def get_turno(t_id):
  print (t_id)
  tur = Turno.query.get_or_404(t_id)
  return turno_schema.jsonify(tur)
  return jsonify(tur.to_dict())
# Read many
@api.route('/turno/', methods=['GET'])
def get_turnos():
  all_turnos = Turno.query.all()
  print ("ALL turnos##",all_turnos,"###777#")
  result = turnos_schema.dump(all_turnos)
  return jsonify(result)
  return jsonify(Turno.to_list(all_turnos))
# Update
@api.route('/turno/<int:t_id>', methods=['PUT'])
def update_turno(t_id):
  data = request.get_json() or {}
  tur = Turno.query.get_or_404(t_id)
  print ("Turno id ####",tur,"#########")
  tur.from_dict(data) # update
  db.session.commit()
  response = jsonify(tur.to_dict())
  response.headers['Location'] = url_for('api.get_turno', t_id=tur.t_id)
  return response, 200
# Delete
@api.route('/turno/<int:t_id>', methods=['DELETE'])
def del_turno(t_id):
  tur = Turno.query.get_or_404(t_id)
  db.session.delete(tur)
  db.session.commit()
  result = {'msg':'Turno deleted',
       'turno':tur.to_dict() }
  response = jsonify(result)
  return response, 200
### create empleado_turno
@api.route('/turno_empleado/<int:t_id>', methods=['GET'])
def get_turno_empleado(t_id):
  print ("#### Turnos asociado al empleado #",t_id)
  empl = Empleado.query.get_or_404(t_id)

  tur = Turno.query.filter(Turno.empleado_id==t_id).all()
  results = turnos_schema.dump(tur)
  print ("Tur results###",tur,'###',results)
  return jsonify(empl.to_dict(),results)#,
# read turno by hora de inicio
@api.route('/turno_hora_inicio/<string:h_inicio>', methods=['GET'])
def get_hora_inicio(h_inicio):
  print ("#### Turnos que inician a la misma hora #",h_inicio)
  tur = Turno.query.filter(Turno.h_entrada==h_inicio).all()
  results = turnos_schema.dump(tur)
  print ("Tur results###",tur,'###',results)
  return jsonify(results)
  # return jsonify({"Prueba":"Hora"})
# read turno by hora de inicio
@api.route('/turno_hora_salida/<string:h_final>', methods=['GET'])
def get_hora_salida(h_final):
  print ("#### Turnos que finalizan a la misma hora #",h_final)
  tur = Turno.query.filter(Turno.h_salida==h_final).all()
  results = turnos_schema.dump(tur)
  print ("Tur results###",tur,'###',results)
  return jsonify(results)

# read turnos que tengan la misma fecha
@api.route('/turno_fecha/<string:fecha_>', methods=['GET'])
def get_tur_fecha(fecha_):
  print ("#### Turnos que tienen la misma fecha #",fecha_)
  tur = Turno.query.filter(Turno.fecha==fecha_).all()
  results = turnos_schema.dump(tur)
  print ("Tur results###",tur,'###',results)
  return jsonify(results)


