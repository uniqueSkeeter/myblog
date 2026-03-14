from flask import Blueprint, request, jsonify
from app import db
from app.models.category import Category
from app.models.article import Article

bp = Blueprint('categories', __name__)

@bp.route('/categories', methods=['GET'])
def get_categories():
    categories = Category.query.all()
    return jsonify([category.to_dict() for category in categories])

@bp.route('/categories', methods=['POST'])
def create_category():
    data = request.get_json()

    if not data or 'name' not in data:
        return jsonify({'error': 'Name is required'}), 400

    if Category.query.filter_by(name=data['name']).first():
        return jsonify({'error': 'Category already exists'}), 400

    category = Category(
        name=data['name'],
        description=data.get('description')
    )

    db.session.add(category)
    db.session.commit()

    return jsonify(category.to_dict()), 201

@bp.route('/categories/<int:id>', methods=['GET'])
def get_category(id):
    category = Category.query.get_or_404(id)
    return jsonify(category.to_dict())

@bp.route('/categories/<int:id>', methods=['PUT'])
def update_category(id):
    category = Category.query.get_or_404(id)
    data = request.get_json()

    if 'name' in data:
        category.name = data['name']
    if 'description' in data:
        category.description = data['description']

    db.session.commit()
    return jsonify(category.to_dict())

@bp.route('/categories/<int:id>', methods=['DELETE'])
def delete_category(id):
    category = Category.query.get_or_404(id)
    db.session.delete(category)
    db.session.commit()
    return '', 204

@bp.route('/categories/<int:id>/articles', methods=['GET'])
def get_articles_by_category(id):
    category = Category.query.get_or_404(id)
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 10, type=int)

    pagination = Article.query.filter_by(category_id=id).order_by(
        Article.created_at.desc()
    ).paginate(page=page, per_page=per_page, error_out=False)

    articles = pagination.items

    return jsonify({
        'articles': [article.to_dict(include_content=False) for article in articles],
        'total': pagination.total,
        'pages': pagination.pages,
        'current_page': page
    })
