import pyexcel
a_list_of_dictionaries = [
    {
        "title" : "Hom nay toi dep",
        "link" : "http://google.com.vn"
    },
    {
        "title" : "Hom nay toi dep",
        "link" : "http://google.com.vn"
    },
    {
        "title" : "Hom nay toi dep",
        "link" : "http://google.com.vn"
    },
]

pyexcel.save_as(records = a_list_of_dictionaries, dest_file_name = "test.xlsx")
