import configparser
import logging
import os

config = configparser.RawConfigParser()
current_dir = os.getcwd()

logging.info("please check config file location: ", f"{current_dir}/configurations/config.ini")

config.read(f"{current_dir}/configurations/config.ini")


class ConfigData:
    @staticmethod
    def get_application_url():
        url = config.get("ApplicationUrl", "qa_url")
        return url

    @staticmethod
    def get_user_name():
        user_name = config.get("Credentials", "QA_username")
        return user_name

    @staticmethod
    def get_password():
        password = config.get("Credentials", "password")
        return password
