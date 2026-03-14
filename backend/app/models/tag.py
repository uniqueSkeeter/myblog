from app import db

article_tags = db.Table('article_tags',
    db.Column('article_id', db.Integer, db.ForeignKey('article.id'), primary_key=True),
    db.Column('tag_id', db.Integer, db.ForeignKey('tag.id'), primary_key=True)
)

class Tag(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False, unique=True)

    articles = db.relationship('Article', secondary=article_tags, back_populates='tags')

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name
        }
