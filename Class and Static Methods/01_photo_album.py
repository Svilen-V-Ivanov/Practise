import math


class PhotoAlbum:
    def __init__(self, pages: int):
        self.pages = pages
        self.photos = [[] for x in range(self.pages)]

    @classmethod
    def from_photos_count(cls, photos_count: int):
        page_count = photos_count / 4
        return cls(math.ceil(page_count))

    def add_photo(self, label: str):
        for index, page in enumerate(self.photos):
            if len(page) < 4:
                #not sure if this is the corrrect way or self.photos[index].append(label)
                page.append(label)
                return f"{label} photo added successfully on page {index + 1} slot {len(page)}"

        return "No more free slots"

    def display(self):
        string = '-----------\n'

        for page in self.photos:
            if not page:
                string += '\n'
            else:
                string += " ".join(str([]) for x in range(len(page))) + '\n'

            string += '-----------\n'

        return string.strip()


album = PhotoAlbum(2)

print(album.add_photo("baby"))
print(album.add_photo("first grade"))
print(album.add_photo("eight grade"))
print(album.add_photo("party with friends"))
print(album.photos)
print(album.add_photo("prom"))
print(album.add_photo("wedding"))

print(album.display())



