class Article:
    def __init__(self,title, content, author):
        self.title=title
        self.author=author
        self.content=content

    def edit(self,new_content):
        self.content=new_content

    def change_author(self,new_author):
        self.author=new_author

    def rename(self, new_title):
        self.title=new_title

    def __repr__(self):
        return f"{self.title} - {self.content}: {self.author}"



'''•	edit(new_content) - changes the old content to the new one
•	change_author(new_author) - changes the old author to with the new one
•	rename(new_title) - changes the old title with the new one
•	__repr__() - returns the following string "{title} - {content}: {author}"
'''
article = Article("some title", "some content", "some author")
article.edit("new content")
article.rename("new title")
article.change_author("new author")
print(article)
