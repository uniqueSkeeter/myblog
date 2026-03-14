from datetime import datetime
from app import db
from app.models.tag import article_tags

class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    content = db.Column(db.Text, nullable=False)
    excerpt = db.Column(db.String(500))
    author = db.Column(db.String(100), default='unique蚊子')
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'))

    tags = db.relationship('Tag', secondary=article_tags, back_populates='articles')

    def to_dict(self, include_content=True):
        data = {
            'id': self.id,
            'title': self.title,
            'excerpt': self.excerpt or self.content[:200] + '...' if self.content else '',
            'author': self.author,
            'created_at': self.created_at.isoformat() if self.created_at else None,
            'updated_at': self.updated_at.isoformat() if self.updated_at else None,
            'category_id': self.category_id,
            'category': self.category.to_dict() if self.category else None,
            'tags': [tag.to_dict() for tag in self.tags]
        }
        if include_content:
            data['content'] = self.content
        return data
