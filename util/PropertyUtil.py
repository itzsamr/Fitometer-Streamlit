import configparser


class PropertyUtil:
    @staticmethod
    def getPropertyString():
        config = configparser.ConfigParser()
        config.read(
            "C:/Users/91915/OneDrive - Valliammai Engineering College/Desktop/Fitometer/util/config.properties"
        )

        server_name = config.get("DATABASE", "server")
        database_name = config.get("DATABASE", "database")
        driver = config.get("DATABASE", "driver")

        return f"DRIVER={{{driver}}};SERVER={server_name};DATABASE={database_name};Trusted_Connection=yes"
