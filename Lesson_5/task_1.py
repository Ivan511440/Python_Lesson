import os


def get_absolute_path(path):
    *_, extension = os.path.splitext(path)
    path_to, _ = os.path.split(path)
    file_name = os.path.basename(path).split('.')[0]
    
    return path_to, file_name, extension


if __name__ == '__main__':
    path = '/Users/Ivan511440/projects/geekbrains/Python_Lesson/Lesson_5/ivan.txt'
    print(get_absolute_path(path))