class Comment:
    def __init__(self, username, text, likes):
        self.username = username
        self.text = text
        self.likes = likes

chelovek = Comment('Masha', 'KRASIVO', 10)
print(chelovek.text)