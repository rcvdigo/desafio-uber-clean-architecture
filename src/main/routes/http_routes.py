# pylint: disable=import-error
from time import sleep
from flask import Blueprint
from flask import request as request_flask
from flask import render_template
from flask import jsonify


# Import from adapters
from src.main.adapters.request_adapter import request_adapter


# Import from composers
from src.main.composers.send_sns_composer import send_sns_composer
from src.main.composers.send_email_composer import send_email_composer
from src.main.composers.sqs_consumer_composer import sqs_consumer_composer
from src.main.composers.email_sns_sender_composer import send_email_sns_composer
from src.main.composers.mongodb_composer_insert import mongodb_composer_insert_html
from src.main.composers.mongodb_composer_insert import mongodb_composer_insert_api
from src.main.composers.mongodb_composer_update import mongodb_composer_update_api
from src.main.composers.postgresql_composer_update import postgresql_composer_update
from src.main.composers.mongodb_composer_select import mongodb_composer_select_api
from src.main.composers.mongodb_composer_delete import mongodb_composer_delete_api
from src.main.composers.postgresql_composer_delete import postgresql_composer_delete_api
from src.main.composers.mongodb_composer_select_id import mongodb_composer_select_id_html
from src.main.composers.postgresql_composer_select_id import postgresql_composer_select_id
from src.main.composers.postgresql_composer_insert import postgresql_composer_insert_api
from src.main.composers.postgresql_composer_insert import postgresql_composer_insert_html
from src.main.composers.postgresql_composer_select import postgresql_composer_select


# Import error handler
from src.main.core.exceptions.error_handler import handler_errors


# Import validators
from src.main.validators.email_validator import email_validator


# Import class HttpResponse
from src.main.core.http_response import HttpResponse


# Apelidando o @app para @email_route_bp
email_route_bp = Blueprint("email_routes", __name__)


@email_route_bp.route("/", methods=["GET"])
def index():
    if request_flask.method == 'GET':
        return render_template('form.html')


@email_route_bp.route("/api/email/", methods=["POST"])
def send_email():
    http_response = None

    try:
        # Protegendo a inserção de dados injetando o validator email_validator
        email_validator(request=request_flask)

        http_response = request_adapter(
            request=request_flask,
            controller=send_email_composer()
        )

    except Exception as exeception:
        http_response = handler_errors(error=exeception)

    return jsonify(http_response.body), http_response.status_code


@email_route_bp.route("/api/email_sns/", methods=["POST"])
def send_email_sns():
    is_request_js = request_flask.headers.get('X-Requested-With')
    if is_request_js == 'XMLHttpRequest':
        try:
            http_response_sns = request_adapter(
                request=request_flask,
                controller=send_email_sns_composer()
            )

            http_response_mongo_db = request_adapter(
                request=request_flask,
                controller=mongodb_composer_insert_html()
            )

            http_response_postgresql = request_adapter(
                request=request_flask,
                controller=postgresql_composer_insert_html()
            )

            if (
                http_response_sns.status_code == 200
                and http_response_mongo_db.status_code == 200
                and http_response_postgresql.status_code == 200
                ):

                http_response = HttpResponse(
                    body={
                        'sns_response': http_response_sns.body,
                        'mongodb_response': http_response_mongo_db.body,
                        'postgresql_response': http_response_postgresql.body,
                        },
                    status_code=200
                )

        except Exception as exeception:
            http_response = handler_errors(error=exeception)
        return jsonify(http_response.body), http_response.status_code
    if is_request_js != 'XMLHttpRequest':
        try:
            # Protegendo a inserção de dados injetando o validator email_validator
            # email_validator(request=request_flask)
            
            http_response_email = request_adapter(
                request=request_flask,
                controller=send_email_composer()
            )

            http_response_sns = request_adapter(
                request=request_flask,
                controller=send_sns_composer()
            )

            http_response_mongo_db = request_adapter(
                request=request_flask,
                controller=mongodb_composer_insert_api()
            )
            
            http_response_postgresql = request_adapter(
                request=request_flask,
                controller=postgresql_composer_insert_api()
            )

            if (
                http_response_email.status_code == 200
                and http_response_sns.status_code == 200
                and http_response_mongo_db.status_code == 200
                and http_response_postgresql.status_code == 200
                ):
                http_response = HttpResponse(
                    status_code=200,
                    body={
                        'email_response': http_response_email.body,
                        'sns_response': http_response_sns.body,
                        'mongobd_response': http_response_mongo_db.body,
                        'postgresql_response': http_response_postgresql.body
                    }
                )

        except Exception as exeception:
            http_response = handler_errors(error=exeception)
        return jsonify(http_response.body), http_response.status_code


@email_route_bp.route("/api/select/", methods=["GET"])
def select():
    # Verifica se o cabeçalho 'Accept' está presente na requisição
    is_request = request_flask.headers.get('Accept')
    if is_request is not None:
        # Divide o cabeçalho 'Accept' para obter o tipo de conteúdo desejado
        is_request = is_request.split(',')[0]

    if is_request == 'text/html':
        
        http_response_mongo = request_adapter(
            request=request_flask,
            controller=mongodb_composer_select_api()
        )

        http_response_postgresql = request_adapter(
            request=request_flask,
            controller=postgresql_composer_select()
        )

        if (
            http_response_mongo.status_code == 200
            and http_response_postgresql.status_code == 200
            ):

            http_response = HttpResponse(
                body={
                    'mongodb_response': http_response_mongo.body,
                    'postgresql_response': http_response_postgresql.body,
                    },
                status_code=200
            )

        return render_template(
            'mongodb_select.html',
            http_response_mongo=http_response.body['mongodb_response'],
            http_response_postgresql=http_response.body['postgresql_response'],
            http_status=http_response.status_code
            )
    
    else:

        http_response_mongo = request_adapter(
            request=request_flask,
            controller=mongodb_composer_select_api()
        )

        http_response_postgresql = request_adapter(
            request=request_flask,
            controller=postgresql_composer_select()
        )

        if (
            http_response_mongo.status_code == 200
            and http_response_postgresql.status_code == 200
            ):

            http_response = HttpResponse(
                body={
                    'mongodb_response': http_response_mongo.body,
                    'postgresql_response': http_response_postgresql.body,
                    },
                status_code=200
            )        

        return jsonify(http_response.body), http_response.status_code
    # Se nenhum dos casos anteriores for atendido, retorna 404
    return jsonify({'error': 'Not Found'}), 404


@email_route_bp.route("/view/<_id>/", methods=["GET"])
def view(_id):
    if 'text/html' in request_flask.headers.get('Accept'):
        # Se for um ObjectID válido do MongoDB
        if len(_id) == 24:

            http_response_mongo = request_adapter(
                request=request_flask,
                controller=mongodb_composer_select_id_html()
            )

            return render_template(
                'view.html',
                http_response=http_response_mongo.body,
                http_status=http_response_mongo.status_code
            )

        # Se for um ID numérico
        elif _id.isdigit():

            http_response_postgresql = request_adapter(
                request=request_flask,
                controller=postgresql_composer_select_id()
            )

            return render_template(
                'view.html',
                http_response=http_response_postgresql.body,
                http_status=http_response_postgresql.status_code
            )

    else:
        if len(_id) == 24:
            
            http_response_mongo = request_adapter(
                request=request_flask,
                controller=mongodb_composer_select_id_html()
            )

            return http_response_mongo.body, http_response_mongo.status_code

        elif _id.isdigit():

            http_response_postgresql = request_adapter(
                    request=request_flask,
                    controller=postgresql_composer_select_id()
                )
            
            return http_response_postgresql.body, http_response_postgresql.status_code


@email_route_bp.route("/api/update/", methods=['POST'])
def update():
    is_request_js = request_flask.headers.get('X-Requested-With')

    if is_request_js == 'XMLHttpRequest':

        if len(request_flask.json['_id']) == 24:

            http_response_mongo = request_adapter(
                request=request_flask,
                controller=mongodb_composer_update_api()
            )

            return jsonify(
                {
                    'status': 'update realizado com sucesso!',
                    'response': http_response_mongo.body
                }), http_response_mongo.status_code

        elif request_flask.json['_id'].isdigit():

            http_response_postgresql = request_adapter(
                request=request_flask,
                controller=postgresql_composer_update()
            )

            return jsonify(
                {
                    'status': 'update realizado com sucesso!',
                    'response': http_response_postgresql.body
                }), http_response_postgresql.status_code

    if is_request_js != 'XMLHttpRequest':

        if len(request_flask.json['_id']) == 24:

            http_response_mongo = request_adapter(
                request=request_flask,
                controller=mongodb_composer_update_api()
            )

            return jsonify(
                {
                    'status': 'update realizado com sucesso!',
                    'response': http_response_mongo.body
                }), http_response_mongo.status_code

        elif request_flask.json['_id'].isdigit():

            http_response_postgresql = request_adapter(
                request=request_flask,
                controller=postgresql_composer_update()
            )

            return jsonify(
                {
                    'status': 'update realizado com sucesso!',
                    'response': http_response_postgresql.body
                }), http_response_postgresql.status_code


@email_route_bp.route("/api/delete/", methods=["POST"])
def delete():
    is_request_js = request_flask.headers.get('X-Requested-With')
    if is_request_js == 'XMLHttpRequest':

        if len(request_flask.json['_id']) == 24:
            
            http_response_mongo = request_adapter(
                request=request_flask,
                controller=mongodb_composer_delete_api()
            )

            return jsonify(
                {
                    'status': 'delete realizado com sucesso!',
                    'response': http_response_mongo.body
                }), http_response_mongo.status_code
        
        elif request_flask.json['_id'].isdigit():

            http_response_postgresql = request_adapter(
                request=request_flask,
                controller=postgresql_composer_delete_api()
            )

            return jsonify(
                {
                    'status': 'delete realizado com sucesso!',
                    'response': http_response_postgresql.body
                }), http_response_postgresql.status_code

    if is_request_js != 'XMLHttpRequest':

        if len(request_flask.json['_id']) == 24:
            http_response_mongo = request_adapter(
                request=request_flask,
                controller=mongodb_composer_delete_api()
            )

            return jsonify(
                {
                    'status': 'delete realizado com sucesso!',
                    'response': http_response_mongo.body
                }), http_response_mongo.status_code
        elif request_flask.json['_id'].isdigit():

            http_response_postgresql = request_adapter(
                request=request_flask,
                controller=postgresql_composer_delete_api()
            )

            return jsonify(
                {
                    'status': 'delete realizado com sucesso!',
                    'response': http_response_postgresql.body
                }), http_response_postgresql.status_code


@email_route_bp.route("/consumer/", methods=["GET"])
def consumer():
    try:    
        http_response_sqs = HttpResponse(
            body=sqs_consumer_composer(),
            status_code=200
        )
        if not http_response_sqs.body['data']:
           while not http_response_sqs.body['data']:
               sleep(20)
               count = 0
               http_response_sqs = HttpResponse(
                   body=sqs_consumer_composer(),
                   status_code=200
               )
               count += 1
               if count == 3:
                   break

        if 'text/html' in request_flask.headers.get('Accept'):
            return render_template(
                'consumer.html',
                messages=http_response_sqs.body,
                status=http_response_sqs.status_code
                )
        else:
            return jsonify(http_response_sqs.body), http_response_sqs.status_code
    except Exception as exeception:
        http_response_sqs = handler_errors(error=exeception)
