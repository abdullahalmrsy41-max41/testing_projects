import configparser
config = configparser.RawConfigParser()
config.read(".\\configurations\\configure.ini")
class ReadProperties:
    @staticmethod
    def get_url():
        url=config.get("properties","url2")
        return url
    @staticmethod
    def get_email():
        email=config.get("properties","email")
        return email
    @staticmethod
    def get_password():
        password=config.get("properties","password")
        return password