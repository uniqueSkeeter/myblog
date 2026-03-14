from flask import Blueprint, request, jsonify
from app import db
from app.models.article import Article
from app.models.tag import Tag

bp = Blueprint('articles', __name__)

@bp.route('/articles', methods=['GET'])
def get_articles():
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 10, type=int)
    category_id = request.args.get('category_id', type=int)
    tag_id = request.args.get('tag_id', type=int)

    query = Article.query

    if category_id:
        query = query.filter_by(category_id=category_id)

    if tag_id:
        query = query.filter(Article.tags.any(id=tag_id))

    pagination = query.order_by(Article.created_at.desc()).paginate(
        page=page, per_page=per_page, error_out=False
    )

    articles = pagination.items

    return jsonify({
        'articles': [article.to_dict(include_content=False) for article in articles],
        'total': pagination.total,
        'pages': pagination.pages,
        'current_page': page
    })

@bp.route('/articles/<int:id>', methods=['GET'])
def get_article(id):
    article = Article.query.get_or_404(id)
    return jsonify(article.to_dict())

@bp.route('/articles', methods=['POST'])
def create_article():
    data = request.get_json()

    if not data or 'title' not in data or 'content' not in data:
        return jsonify({'error': 'Title and content are required'}), 400

    article = Article(
        title=data['title'],
        content=data['content'],
        excerpt=data.get('excerpt'),
        author=data.get('author', 'unique蚊子'),
        category_id=data.get('category_id')
    )

    if 'tag_ids' in data:
        tags = Tag.query.filter(Tag.id.in_(data['tag_ids'])).all()
        article.tags = tags

    db.session.add(article)
    db.session.commit()

    return jsonify(article.to_dict()), 201

@bp.route('/articles/<int:id>', methods=['PUT'])
def update_article(id):
    article = Article.query.get_or_404(id)
    data = request.get_json()

    if 'title' in data:
        article.title = data['title']
    if 'content' in data:
        article.content = data['content']
    if 'excerpt' in data:
        article.excerpt = data['excerpt']
    if 'author' in data:
        article.author = data['author']
    if 'category_id' in data:
        article.category_id = data['category_id']
    if 'tag_ids' in data:
        tags = Tag.query.filter(Tag.id.in_(data['tag_ids'])).all()
        article.tags = tags

    db.session.commit()
    return jsonify(article.to_dict())

@bp.route('/articles/<int:id>', methods=['DELETE'])
def delete_article(id):
    article = Article.query.get_or_404(id)
    db.session.delete(article)
    db.session.commit()
    return '', 204
