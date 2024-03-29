import json
import datetime as dt


class jsonParse(object):
    def __init__(self, name):
        name_split = name.split(".")

        file_suffix = 'json'
        if name_split[-1] != file_suffix:
            raise SyntaxError

        with open(name, 'r+') as f:
            self.data = json.load(f)

    @staticmethod
    def transform_date_to_excel(date):
        excel_base_date = dt.datetime(1899, 12, 30)
        delta = date - excel_base_date
        # excel_serial_date = delta.days + delta.seconds / (24 * 60 * 60)
        excel_serial_date = delta.days + 0.62569
        return excel_serial_date

    @staticmethod
    def transform_date_to_excel_int(date):
        excel_base_date = dt.datetime(1899, 12, 30)
        delta = date - excel_base_date
        excel_serial_date = delta.days
        return excel_serial_date

    @staticmethod
    def transform_str_to_date(str_date):
        date_date = dt.datetime.strptime(str_date, "%Y%m%d")
        return date_date

    def transform_int_to_date(self, int_date):
        str_date = str(int_date)
        date_date = self.transform_str_to_date(str_date)
        return date_date

    @staticmethod
    def str_to_bool(str_bool):
        if str_bool == "true":
            flag = 1
        else:
            flag = 0
            return flag

    def get_pricing_date(self):
        general_args = self.data[0]['generalArgs']

        pricing_days = general_args['pricingDays']

        pricing_days = dt.datetime.strptime(pricing_days[0], "%Y%m%d")

        pricing_days_excel = self.transform_str_to_date(pricing_days)

        return pricing_days_excel

    def get_issue_date(self):
        general_args = self.data[0]['generalArgs']

        issue_date = dt.datetime.strptime(general_args["issueDate"][0:8], "%Y%m%d")

        issue_date_excel = self.transform_date_to_excel_int(issue_date)

        return issue_date_excel

    @staticmethod
    def get_expiry_date(data_json):
        general_args = data_json[0]['generalArgs']

        expiry_date = dt.datetime.strptime(general_args["expiryDate"][0:8], "%Y%m%d")

        return expiry_date

    @staticmethod
    def get_holiday(data_json):
        market_args = data_json[0]["marketUdArgs"]

        holidays = market_args["holidays"]

        return holidays

    def get_obv_days(self):
        obv_days = self.data[0]["obvDays"]

        obv_days_ = [self.transform_date_to_excel_int(self.transform_int_to_date(day)) for day in obv_days]

        return obv_days_

    def get_ki_obv_days(self):
        ki_obv_days = self.data[0]["kiObvDays"]

        ki_obv_days = [self.transform_date_to_excel_int(self.transform_int_to_date(day)) for day in ki_obv_days]

        return ki_obv_days

    def get_coupon_obv_days(self):
        coupon_obv_days = self.data[0]["paymentObvDays"]

        coupon_obv_days = [self.transform_date_to_excel_int(self.transform_int_to_date(day)) for day in coupon_obv_days]

        return coupon_obv_days

    @staticmethod
    def get_pricing_method(data_json):
        general_args = data_json[0]['generalArgs']

        pricing_method = general_args["pricingMethod"]

        if pricing_method == 'MONTECARLO':
            pricing_method = 0
        else:
            pricing_method = 1

        return pricing_method

    