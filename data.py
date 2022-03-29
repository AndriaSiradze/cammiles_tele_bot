import shelve

file_name = 'data_base'

test_data = {'#borjomi': ['AQADo70xG6K4mUl4', 'AQADo70xG6K4mUly', 'AQADo70xG6K4mUl9']}  # '


def write_db(new_data):
    with shelve.open(file_name) as db:
        for hashtag, file_ids_list in new_data.items():
            if hashtag not in db.keys():  # if not key in data base making key + values
                db[hashtag] = file_ids_list
            if hashtag in db.keys():  # if key in data base appending new file ids to data base
                in_db = set(db[hashtag])
                to_append = set(file_ids_list)
                db[hashtag] = list(in_db | to_append)


def check_data():
    with shelve.open(file_name) as db:
        result = f'keys : {list(db.keys())} \n' \
                 f'items : {list(db.values())}\n'
        return result

def read_db():
    with shelve.open(file_name) as db:
        return dict(db)

def clear_db():
    with shelve.open(file_name) as db:
        db.clear()



if __name__ == "__main__":
    write_db(test_data)
    read_db()
