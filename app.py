from flask import Flask,request,jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return jsonify(message="Home Page")

# In-memory data store
items = [{"id": 1, "name": "This is item 1"}, {"id": 2, "name": "This is item 2"}]

# Get all items
@app.route('/api/items', methods=['GET'],strict_slashes=False)
def get_items():
    return jsonify(items)

# Get by id
@app.route('/api/items/<int:item_id>', methods=['GET'], strict_slashes=False)
def get_item_by_id(item_id):
    for item in items:
        if item['id'] == item_id:
            return jsonify(item)
    return jsonify(message='Nothing Found!'), 404

# Create new item
@app.route('/api/items', methods=['POST'], strict_slashes=False)
def create_item():
    json_data = request.get_json()
    new_item = {'id':json_data['id'],'name':json_data['name']}
    items.append(new_item)
    return jsonify(new_item),201

# Update item
@app.route('/api/items/<int:item_id>', methods=['PUT'], strict_slashes=False)
def update_item(item_id):
    for item in items:
        if item['id'] == item_id:
            item['name'] = request.get_json()['name']
            return jsonify(item)
    return jsonify(message='Nothing Found'),404

# Delete item
@app.route('/api/items/<int:item_id>', methods=['DELETE'], strict_slashes=False)
def delete_item(item_id):
    global items
    new_items = []
    for item in items:
        if item['id'] == item_id:
            continue
        new_items.append(item)
    items = new_items
    return jsonify(message='Deleted'),204

if __name__ == "__main__":
    app.run(debug=True)