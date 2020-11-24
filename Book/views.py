from django.shortcuts import render

# Create your views here.


# chapter list view
# have to style it as card view 
def chapter_index(request):
    return render(request, 'Book/chapter_index.html')



def chapter(request, num):

    # chapter_list is containing list of all chapters
    # rendering template by taking num as url input from chapter_index.html
    chapter_list = {
        1: 'chap/chap1.html',
        2: 'chap/chap2.html',
        3: 'chap/chap3.html',
        4: 'chap/chap4.html',
        5: 'chap/chap5.html',
        6: 'chap/chap6.html',
        7: 'chap/chap7.html',
        8: 'chap/chap8.html',
        9: 'chap/chap9.html',
        10: 'chap/chap10.html',
        11: 'chap/chap11.html',
        12: 'chap/chap12.html',
        13: 'chap/chap13.html',
        14: 'chap/chap14.html',
        15: 'chap/chap15.html'
    }
    return render(request, chapter_list[int(num)])