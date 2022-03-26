import os


# def extract_place(filename):
#     first = filename.find("_")
#     partial = filename[first+1:]
#     second = partial.find("_")
#     return partial[:second]


# def extract_place(filename):
#     return filename.split("_")[1]
# text = filename.split("_")
# place_name = text[1]
# return place_name
# print(extract_place("2016-11-04_Berlin_09/42/22.jpg"))
# print(extract_place("2018-01-03_Oahu_21/51/57.jpg"))
# print(extract_place("2018-01_Scotland_11/51/27.jpg"))

def make_place_directories(places): # Here's the function definition
    for place in places:
        os.mkdir(place)

def extract_place(filename):
    return filename.split('_')[1]

def organize_photos(directory):
    os.chdir(directory)
    originals = os.listdir()
    places = []
    for filename in originals:
        place = extract_place(filename)
        if place not in places: # This is the key change
            places.append(place)

    make_place_directories(places)

    for filename in originals:
        place = extract_place(filename)
        os.rename(filename, os.path.join(place, filename))

organize_photos("Photos")
