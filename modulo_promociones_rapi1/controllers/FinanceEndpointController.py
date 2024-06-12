import requests
from flask import Blueprint, request, jsonify

burop_bp = Blueprint('rapi_burop_GET', __name__)
mpagp_bp = Blueprint('rapi_mpagp_GET', __name__)
dtpro_bp = Blueprint('rapi_dtpro_GET', __name__)

__URL__ = '/rest/getdata-modulos-promocionales-api/v1.0/finance'


class FinanceEndpointController:
    @burop_bp.route(__URL__+'/buro', methods=['GET'])
    def burop_endpoint():
        try:
            print("\nFinancial - Buro")
            print("Fase de Escucha | FRONT-ENDPOINT ACTIVADO")
            print("COMBO ENDPOINT ACTIVO\n")
            _type = request.args.get('type')
            if _type == 'ALL_BURO':
                params = {'type': _type}
                headers = {'Referer': __URL__ + '/buro'}
                response = requests.get('http://localhost:5012/api/ra/plcback_endpoint', params=params,
                                        headers=headers)
                return response.text, response.status_code
            else:
                print("burop_endpoint - FrontEndpointController | Tipo de Petición no válido")
                return jsonify({'error': 'Tipo de petición no válido'}), 400
        except Exception as e:
            print("--------------------------------------------------------------------")
            print("burop_endpoint - FrontEndpointController | Error Detectado: ", e)
            print("--------------------------------------------------------------------")
            return jsonify({'Error': e})

    @mpagp_bp.route(__URL__+'/modos-pago', methods=['GET'])
    def mpagp_endpoint():
        try:
            print("\nFinancial - Modos de Pago")
            print("Fase de Escucha | FRONT-ENDPOINT ACTIVADO")
            print("COMBO ENDPOINT ACTIVO\n")
            _type = request.args.get('type')
            if _type == 'ALL_MPAGOS':
                params = {'type': _type}
                headers = {'Referer': __URL__ + '/modos-pago'}
                response = requests.get('http://localhost:5012/api/ra/plcback_endpoint', params=params,
                                        headers=headers)
                return response.text, response.status_code
            else:
                print("mpagp_endpoint - FrontEndpointController | Tipo de Petición no válido")
                return jsonify({'error': 'Tipo de petición no válido'}), 400
        except Exception as e:
            print("--------------------------------------------------------------------")
            print("mpagp_endpoint - FrontEndpointController | Error Detectado: ", e)
            print("--------------------------------------------------------------------")
            return jsonify({'Error': e})

    @dtpro_bp.route(__URL__+'/datos-promocionales', methods=['GET'])
    def dtpro_endpoint():
        try:
            print("\nFinancial - Data Promocional")
            print("Fase de Escucha | FRONT-ENDPOINT ACTIVADO")
            print("COMBO ENDPOINT ACTIVO\n")
            _type = request.args.get('type')
            valid_type = {"DIAS_GOZADOS", "PRECIO_REGULAR", "UPGRADE"}
            if _type in valid_type:
                params = {'type': _type}
                if 'TARIFFPLAN' in request.args:
                    params['_V1'] = request.args.get('TARIFFPLAN')
                    if 'TARIFFPLANVARIANT' in request.args:
                        params['_V2'] = request.args.get('TARIFFPLANVARIANT')
                if 'TARIFFPLANVARIANT' in request.args and '_V1' not in params:
                    params['_V1'] = request.args.get('TARIFFPLANVARIANT')
                    if 'id_Prod' in request.args:
                        params['_V2'] = request.args.get('id_Prod')
                headers = {'Referer': __URL__ + '/datos-promocionales'}
                response = requests.get('http://localhost:5012/api/ra/plcback_endpoint', params=params,
                                        headers=headers)
                return response.text, response.status_code
            else:
                print("mpagp_endpoint - FrontEndpointController | Tipo de Petición no válido")
                return jsonify({'error': 'Tipo de petición no válido'}), 400
        except Exception as e:
            print("--------------------------------------------------------------------")
            print("dtpro_endpoint - FrontEndpointController | Error Detectado: ", e)
            print("--------------------------------------------------------------------")
            return jsonify({'Error': e})
