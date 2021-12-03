
'''
Settings for HBNet Web Server.
'''
# Database options
# Using SQLite is simple and easiest. Comment out this line and uncomment the MySQL
# line to use a MySQL/MariaDB server.
db_location = 'sqlite:////opt/hbnet_web/data/hbnet.sqlite'

# Uncomment and change this line to use a MySQL DB. It is best to start with a fresh
# DB without data in it.

#db_location = 'mysql+pymysql://DB_USERNAME:DB_PASSWORD@DB_HOST:MySQL_PORT/DB_NAME'


# Title of the HBNet Web Service/DMR network
title = 'HBNet Web Service (Docker, Unconfigured)'
# Port to run server
hws_port = 8080
# IP to run server on
hws_host = '127.0.0.1'
# Publicly accessible URL of the web server. THIS IS REQUIRED AND MUST BE CORRECT.
url = 'http://localhost:8080'
# Replace below with some random string such as an SHA256
secret_key = '123456789123456789123456789123456789123456789123456789'

# Timezone to show time stamps in. Stored in DB as UTC. Offset in hours.
hbnet_tz = -1

# Time format for display on some pages
time_format = '%H:%M:%S - %m/%d/%y'

# Default state for newly created user accounts. Setting to False will require
# the approval of an admin user before the user can login.
default_account_state = True

# Legacy passphrase used in hblink.cfg
legacy_passphrase = 'passw0rd'

# Coordinates to center map over
center_map = [45.372, -121.6972]
# Default map zoom level
map_zoom = 5

# Passphrase calculation config. If REMOTE_CONFIG is not used in your DMR server config
# (hblink.cfg), then the values in section [USER_MANAGER] MUST match the values below.
# If REMOTE_CONFIG is enabled, the DMR server (hblink) will automatically use the values below.
# These config options affect the generation of user passphrases.

# Set to a value between 1 - 99. This value is used in the normal calculation.
append_int = 1

# Set to a value between 1 - 99. This value is used for compromised passphrases.
burn_int = 5

# Set to a value between 1 - 99 This value is used in the normal calculation.
extra_int_1 = 5

# Set to a value between 1 - 99 This value is used in the normal calculation.
extra_int_2 = 8

# Set to a length of about 10 characters.
extra_1 = 'TeSt'
extra_2 = 'DmR4'

# Shorten generated passphrases
use_short_passphrase = True

# Character length of shortened passphrase
shorten_length = 6
# How often to pick character from long passphrase when shortening.
shorten_sample = 4

# Email settings
MAIL_SERVER = 'smtp.gmail.com'
MAIL_PORT = 465
MAIL_USE_SSL = True
MAIL_USE_TLS = False
MAIL_USERNAME = 'app@gmail.com'
MAIL_PASSWORD = 'password'
MAIL_DEFAULT_SENDER = '"' + title + '" <app@gmail.com>'

# User settings settings
USER_ENABLE_EMAIL = True
USER_ENABLE_USERNAME = True    
USER_REQUIRE_RETYPE_PASSWORD = True 
USER_ENABLE_CHANGE_USERNAME = False
USER_ENABLE_MULTIPLE_EMAILS = True
USER_ENABLE_CONFIRM_EMAIL = True
USER_ENABLE_REGISTER = True
USER_AUTO_LOGIN_AFTER_CONFIRM = False
USER_SHOW_USERNAME_DOES_NOT_EXIST = True


