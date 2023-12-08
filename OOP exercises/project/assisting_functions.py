def get_details(type, title, year, age_restriction, likes, user_username):
    return f"{type} - Title:{title}, Year:{year}, " \
           f"Age restriction:{age_restriction}, Likes:{likes}, Owned by:{user_username}"


def get_user(name, list):
    for item in list:
        if item.username == name:
            return item

    return None


def get_dict_items(movie, dict):
    for key, value in dict.items():
        if key == 'title':
            movie.title = value
        elif key == 'year':
            movie.year = value
        elif key == 'age_restriction':
            movie.age_restriction = value