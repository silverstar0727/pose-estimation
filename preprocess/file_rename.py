import os

for i in range(204):
    old_name = f"./학습x/{i}.jpg"
    if i < 10:
        new_name = f"./x/image_00{i}.jpg"
    elif 10 <= i < 100:
        new_name = f"./x/image_0{i}.jpg"
    else:
        new_name = f"./x/image_{i}.jpg"

    try:
        os.rename(old_name, new_name)
        print(i)
    except:
        pass