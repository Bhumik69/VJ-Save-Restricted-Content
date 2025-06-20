import os

BOT_TOKEN = "8094935353:AAG_ESPRK21dcWlI0Bw4gLEAl2URnveQqUY"
API_ID = 23644766
API_HASH = "9dc15dd41be1a26016b2ebac611868f5"

# Your Owner / Admin Id For Broadcast 
ADMINS = 6982977861

# Your Mongodb Database Url
# Warning - Give Db uri in deploy server environment variable, don't give in repo.
DB_URI = "mongodb+srv://Group-management:h28hYvrDpnSEcBc8@cluster.2e4dvo1.mongodb.net/groupdb?retryWrites=true&w=majority&tls=true" # Warning - Give Db uri in deploy server environment variable, don't give in repo.
DB_NAME = "groupdb"

# If You Want Error Message In Your Personal Message Then Turn It True Else If You Don't Want Then Flase
ERROR_MESSAGE = bool(os.environ.get('ERROR_MESSAGE', True))
