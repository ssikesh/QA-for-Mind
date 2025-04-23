import configparser

config = configparser.RawConfigParser()
config.read(".//Configurations//config.ini")

class ReadConfig:
    @staticmethod
    def geturl():
        url = config.get("common information","BaseUrl")
        return url

    @staticmethod
    def getname():
        name = config.get("common information","name")
        return name

    @staticmethod
    def getemail():
        email = config.get("common information","email")
        return email

    @staticmethod
    def getphone():
        phone = config.get("common information","phone")
        return phone

    @staticmethod
    def getinterest():
        interest = config.get("common information","interest")
        return interest

    @staticmethod
    def getcompany():
        company = config.get("common information","company")
        return company

    @staticmethod
    def getany_queries():
        any_queries = config.get("common information","any_queries")
        return any_queries
