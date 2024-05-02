from flask import Flask,render_template,request

app = Flask(__name__)




@app.route('/',methods=['GET','POST'])
def home():
    return render_template('index.html')

@app.route('/book/<int:book_id>',methods=['GET','POST'])
def book(book_id):
    book = {
        "book": "Harry Poter",
        "Author": "J.K.Rowling",
        "Published": 1995
    }
    book1 = {
        "book": "Sherlock Holmes",
        "Author": "Arthur Conan Doyle",
        "Published": "1887"
    }
    book2 = {
        "book": "Murder On The  Orient Express",
        "Author": "Agatha Christie",
        "Published": 1934
    }
    return render_template('book.html',bo=book,bo1=book1,bo2=book2  )


@app.route('/add_book',methods=['GET','POST'])
def add_book():

    return render_template('add_book.html')






if __name__=='__main__':
    app.run(debug=True)
