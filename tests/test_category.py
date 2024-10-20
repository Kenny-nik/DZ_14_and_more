from src.category import Category
from src.product import Product
def test_category_init():
    category = Category("Test Category", "Test Description", [])
    assert category.name == "Test Category"
    assert category.description == "Test Description"
    assert category.products == []
def test_category_count():
    Category("Category 1", "Description of category 1", [])
    Category("Category 2", "Description of category 2", [])
    assert Category.category_count == 0

def test_product_count():
    product1 = Product("Product 1", "Description 1", 99.99, 10)
    product2 = Product("Product 2", "Description 2", 199.99, 5)
    category = Category("Test Category", "Test Description", [])
    category.add_product(product1)
    category.add_product(product2)
    assert Category.product_count == 4

#работаем
