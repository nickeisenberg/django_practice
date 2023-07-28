from django.core.paginator import Paginator

posts = ['1', '2', '3', '4', '5']

p = Paginator(posts, 2)

p.num_pages

for page in p.page_range:
    print(page)

p1 = p.page(1)

p1.number

p1.object_list

p1.has_previous()
p1.has_next()

p1.next_page_number()
