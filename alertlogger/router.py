# ## Only required if there are multiple DBs
# import random

# class DatabaseRouter:
#   def db_for_read(self, model, **hints):
#     return random.choice(['replica_1', 'replica_2'])

#   def db_for_write(self, model, **hints):
#     return 'default'

#   def allow_relation(self, obj1, obj2, **hints):
#     return True

#   def allow_migrate(self, db, app_label, model_name=None, **hints):
#     return True
