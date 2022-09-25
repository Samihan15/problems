region_list = [
    # column
     ['us',    'canada'] # row
    ,['india', 'china']
    ,['uk',    'france']
]

# print(region_list[1][0])

for region in region_list:
    for country in region:
        if country == 'india':
            print('I love india')

        # print(country)

