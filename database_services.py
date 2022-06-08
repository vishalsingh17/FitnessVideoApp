import harperdb
import config

url = 'https://fitnessapp-vishal.harperdbcloud.com'

db = harperdb.HarperDB(url=url, username=config.HARPERDB_USERNAME, password=config.HARPERDB_PASSWORD)

SCHEMA = 'workout_repo'
TABLE = 'workouts'
TABLE_TODAY = 'workout_today'

data = {
    'video_id': '123',
    'title': 'Test1'
}

def insert_data(workout_data):
    return db.insert(SCHEMA, TABLE, [workout_data])

def delete_workout(workout_id):
    return db.delete(SCHEMA, TABLE, [workout_id])

def get_all_workout(workout_id):
    return db.sql(f'SELECT video_id, channel, title, duration FROM {SCHEMA}.{TABLE}')



