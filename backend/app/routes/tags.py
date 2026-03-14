from flask import Blueprint, request, jsonify
from app import db
from app.models.tag import Tag
from app.models.article import Article

bp = Blueprint('tags', __name__)

@bp.route('/tags', methods=['GET'])
def get_tags():
    tags = Tag.query.all()
    return jsonify([tag.to_dict() for tag in tags])

@bp.route('/tags', methods=['POST'])
def create_tag():
    data = request.get_json()

    if not data or 'name' not in data:
        return jsonify({'error': 'Name is required'}), 400

    if Tag.query.filter_by(name=data['name']).first():
        return jsonify({'error': 'Tag already exists'}), 400

    tag = Tag(name=data['name'])

    db.session.add(tag)
    db.session.commit()

    return jsonify(tag.to_dict()), 201

@bp.route('/tags/<int:id>', methods=['GET'])
def get_tag(id):
    tag = Tag.query.get_or_404(id)
    return jsonify(tag.to_dict())

@bp.route('/tags/<int:id>', methods=['PUT'])
def update_tag(id):
    tag = Tag.query.get_or_404(id)
    data = request.get_json()

    if 'name' in data:
        tag.name = data['name']

    db.session.commit()
    return jsonify(tag.to_dict())

@bp.route('/tags/<int:id>', methods=['DELETE'])
def delete_tag(id):
    tag = Tag.query.get_or_404(id)
    db.session.delete(tag)
    db.session.commit()
    return '', 204

@bp.route('/tags/<int:id>/articles', methods=['GET'])
def get_articles_by_tag(id):
    tag = Tag.query.get_or_404(id)
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 10, type=int)

    pagination = Article.query.filter(Article.tags.any(id=id)).order_by(
        Article.created_at.desc()
    ).paginate(page=page, per_page=per_page, error_out=False)

    articles = pagination.items

    return jsonify({
        'articles': [article.to_dict(include_content=False) for article in articles],
        'total': pagination.total,
        'pages': pagination.pages,
        'current_page': page
    })
