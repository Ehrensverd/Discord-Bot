import db_handler
class BotOperator:
    """Bot operator
     important fucntions that read, insert to database as well as
     process data from both discord and database.

     """
    pass

    def __init__(self):
        pass


    def sync_members(self, members):
        """Ensures database data is synced and  up to date with discord members"""
        for k, v in members.items():
            print(k, '---->', v.name, '  :   ', v.id, '      ', v.discriminator)

        #Return true if db sync was performed or not needed, false if db could not be reached or changed
        return

    def insert_user(self, user):
        """Prefors a insert query and tries to write single user to database by id"""
        db_handler.insert_user(user)

    def insert_users(self, users):
        """Similar to insert user, but inserts multiple users."""
        db_handler.insert_users(users)



    def update_user(self, user):
        """Changes name and / or discirinator of existing user. does not change ID"""
        db_handler.update_user(user)

    def retrieve_db_members(self):
        """Preforms a query and retrieves members as a list"""

        return db_handler.members()
