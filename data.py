import shelve

file_name = 'data_base'


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


def show_names():
    with shelve.open(file_name) as db:
        return [key for key in db]


def get_ids(key):
    with shelve.open(file_name) as db:
        return [photo_id for photo_id in db[key]]


def clear_db():
    with shelve.open(file_name) as db:
        db.clear()


if __name__ == "__main__":
    print(show_names())
    clear_db()
