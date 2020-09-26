from flask import jsonify
from werkzeug.http import HTTP_STATUS_CODES


def error_response(status_code, message=None):
  payload = {'error': HTTP_STATUS_CODES.get(status_code, 'Unknown error')}
  if message:
      payload['message'] = message
  response = jsonify(payload)
  response.status_code = status_code
  return response


def bad_request(message):
  return error_response(400, message)


from api import api

all_methods = ['GET', 'POST', 'PUT', 'PATCH', 'DELETE']
#all_methods+= ['HEAD','OPTIONS']

@api.app_errorhandler(400)
def bad_request_(err, methods=all_methods):
  print(err)
  return error_response(400, 'Bad Request.')

@api.app_errorhandler(404)
def not_found(err, methods=all_methods):
  print(err)
  return error_response(404, 'The resource could not be found.')

@api.app_errorhandler(405)
def not_found(err, methods=all_methods):
  print(err)
  return error_response(405, 'The method is not allowed for the requested URL.')

@api.app_errorhandler(500)
def internal_error(err, methods=all_methods):
  print(err)
  return error_response(500, 'Something goes wrong.')
