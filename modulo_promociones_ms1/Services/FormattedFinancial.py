from flask import jsonify


class FormattedFinance:
    @staticmethod
    def formatted_financial(_type: str, data):
        try:
            json_data = {}

            if _type == "ALL_BURO":
                json_data['BURO'] = []
                for buro in data['BURO']:
                    json_data['BURO'].append({
                        'ID': buro.ID,
                        'NAME': buro.NAME
                    })

            if _type == "ALL_MPAGOS":
                json_data['MPAGOS'] = []
                for mpagos in data['MPAGOS']:
                    json_data['MPAGOS'].append({
                        'ID': mpagos.ID,
                        'NAME': mpagos.NAME
                    })

            if _type == "UPGRADE":
                json_data['UPGRADE'] = []
                for dt in data['UPGRADE']:
                    json_data['UPGRADE'].append({
                        'ID': dt.ID,
                        'NAME': dt.NAME
                    })
            if _type == "PRECIO_REGULAR":
                json_data['PRECIO_REGULAR'] = []
                for dt in data['PRECIO_REGULAR']:
                    json_data['PRECIO_REGULAR'].append({
                        'PRECIO': dt.PRECIO
                    })

            if _type == "DIAS_GOZADOS":
                json_data['DIAS_GOZADOS'] = []
                for dt in data['DIAS_GOZADOS']:
                    json_data['DIAS_GOZADOS'].append({
                        'ID': dt.ID,
                        'NAME': dt.NAME
                    })

            return json_data

        except Exception as e:
            print("--------------------------------------------------------------------")
            print("FormattedFinance - formatted_financial | Error: ", e)
            print("--------------------------------------------------------------------")
            return jsonify({'Error': str(e)})


