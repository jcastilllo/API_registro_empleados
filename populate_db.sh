serv='http://localhost:5000/api'
tur="$serv/turno"
empl="$serv/empleado"
turno_empleado="$serv/turno_empleado"
hora_inicio="$serv/turno_hora_inicio"
hora_salida="$serv/turno_hora_salida"
tur_fecha="$serv/turno_fecha"

###### CREATE #######
http POST $empl/ empleado_id=149048900 nombre=Mauricio apellido=Castillo
http POST $empl/ empleado_id=183308261 nombre=Jose apellido=Rivera
http POST $empl/ empleado_id=803456693 nombre=Esther apellido=Mendoza
http POST $empl/ empleado_id=159016115 nombre=Judith apellido=Martinez
http POST $empl/ empleado_id=254765706 nombre=Ninoska apellido=Perdomo
http POST $empl/ empleado_id=190484996 nombre=Omaira apellido=Espinoza
http POST $empl/ empleado_id=25475506 nombre=Zenaida apellido=Salas

http POST $tur/ h_entrada=8:00 h_salida=15:30 fecha=2020-06-01 empleado_id=19048900
http POST $tur/ h_entrada=8:00 h_salida=15:30 fecha=2020-06-01 empleado_id=18308261
http POST $tur/ h_entrada=8:00 h_salida=15:30 fecha=2020-06-01 empleado_id=8036693
http POST $tur/ h_entrada=3:30 h_salida=23:30 fecha=2020-08-02 empleado_id=15901115
http POST $tur/ h_entrada=3:30 h_salida=23:30 fecha=2020-08-02 empleado_id=25475506
http POST $tur/ h_entrada=3:30 h_salida=23:30 fecha=2020-08-02 empleado_id=19048996
http POST $tur/ h_entrada=12:00 h_salida=20:00 fecha=2020-08-03 empleado_id=10789526
http POST $tur/ h_entrada=12:00 h_salida=20:00 fecha=2020-08-03 empleado_id=19048900
http POST $tur/ h_entrada=12:00 h_salida=20:00 fecha=2020-06-03 empleado_id=8036693

http GET $empl/
http GET $tur/
#### READ #####
## http://localhost:5000/api/empleado/   ### show empleados list
## http://localhost:5000/api/turno		### show turnos list
http GET $empl/4
http GET $tur/1
http GET $turno_empleado/1

#### update
http PUT $empl/19048900 nombre='MAURICIO' apellido='CASTILLO SANCHEZ'
http PUT $tur/3 h_entrada='00:00' h_salida='23:00' fecha='2020-09-22' empleado='1'
##### delete

http DELETE $tur/3
http DELETE $empl/7

#consulta de tunos asociados al empleado
http GET $turno_empleado/19048901

#consulta de tunos que comienzan y terminan a la misma hora
http GET $hora_inicio/22:00
http GET $hora_salida/11:30

http GET $tur_fecha/2020-06-03
#Product.query.filter_by(price<300)
#Product.query.filter_by(qty<500)
#Product.query.filter_by(cate_id=5)
