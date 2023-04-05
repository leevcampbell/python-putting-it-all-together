#!/usr/bin/env python3

class Book:
    def __init__(self, title, page_count=0):
        self.title = title
        self.page_count = page_count

    def get_page_count(self):
        return self._page_count
    
    def set_page_count(self, page_count):
        if not isinstance(page_count, int):
            print("page_count must be an integer")
        else:
            self._page_count = page_count

    page_count = property(get_page_count, set_page_count)

    def turn_page(self):
        print("Flipping the page...wow, you read fast!")
        

        
# the_shadow_of_the_wind = Book()
       
        
