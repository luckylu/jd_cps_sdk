class Config:
    __instance = None

    def get_instance():
        return Config.__instance

    def __init__(self, app_key, app_secret):
        if Config.__instance != None:
            raise Exception("can not init multi instances")
        else:
            self.app_key = app_key
            self.app_secret = app_secret
            Config.__instance = self
