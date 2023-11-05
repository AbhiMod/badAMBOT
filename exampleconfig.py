from sample_config import Config


class Development(Config):
    # get this values from the my.telegram.org
    APP_ID = 27733303
    API_HASH = "c3c9d5e5d89c99fb8bb85a22a0cb5a26"
    # the name to display in your alive message
    ALIVE_NAME = "𝓐𝓜𝓑𝓞𝓣"
    # create any PostgreSQL database (i recommend to use elephantsql) and paste that link here
    DB_URI = "postgres://yone:Kushal55@yone.cirqmtrbghab.us-east-1.rds.amazonaws.com:5432/yone"
    # After cloning the repo and installing requirements do python3 stringsetup.py an fill that value with this
    STRING_SESSION = "1BVtsOMgBu8OWJoRux4Z9v75VLfGhU3b6GDGK28A5RLMxV7I4bAF9Ie3kSFXgcGLVl5yL6X72hfcRVhiZW9sVXGwaEqK41MlZdwGBM34CHhoAVmxJyWwJgn5jYILPbFPLNAmwyg-Dh4w7NzYsv1-SkRaqNeoNSTuDKzHt3CiSufmjPyr8Bn1whWFHMbgIAdR5IWbG6eSNCNXCsbWKsSjk26WjTmjRGhMNmtNkGnT49o_44a0JRHjtaV-ZxK3VJODp0wfF9Dm1Vs4q_ZJAtlzfnfz6XVSQw5IuM5MupCGjXONrDknCvU-BjyQA1pJYjP91rXapNiwoWZEPRezC8gcL1nEyKoYecrY="
    # create a new bot in @botfather and fill the following vales with bottoken
    TG_BOT_TOKEN = "6025897464:AAHzfh1RbybhNUzIs1W8yATQ6jQdRAgc9bM"
    # create a private group and a rose bot to it and type /id and paste that id here (replace that -100 with that group id)
    PRIVATE_GROUP_BOT_API_ID = -1002076281896
    # command handler
    COMMAND_HAND_LER = "."
    # command hanler for sudo
    SUDO_COMMAND_HAND_LER = "."
    # External plugins repo
    EXTERNAL_REPO = "https://github.com/AbhiMod/CatPlugins"
    # if you need badcat plugins set "True"
    BADCAT = "True"
