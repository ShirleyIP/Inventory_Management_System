import sqlite3
from datetime import datetime

def create_tables():
    conn = sqlite3.connect('inventory_management_v3.db')  # Consistent DB name
    cursor = conn.cursor()
    
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS categories (
        category_id INTEGER PRIMARY KEY AUTOINCREMENT,
        category_name TEXT NOT NULL,
        description TEXT
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS suppliers (
        supplier_id INTEGER PRIMARY KEY AUTOINCREMENT,
        supplier_name TEXT NOT NULL,
        contact_info TEXT,
        address TEXT
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS products (
        product_id INTEGER PRIMARY KEY AUTOINCREMENT,
        product_name TEXT NOT NULL,
        category_id INTEGER,
        supplier_id INTEGER,
        stock_level INTEGER NOT NULL,
        reorder_level INTEGER NOT NULL,
        price REAL NOT NULL,
        date_added DATE NOT NULL,
        FOREIGN KEY (category_id) REFERENCES categories (category_id),
        FOREIGN KEY (supplier_id) REFERENCES suppliers (supplier_id)
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS sales (
        sale_id INTEGER PRIMARY KEY AUTOINCREMENT,
        product_id INTEGER,
        quantity_sold INTEGER NOT NULL,
        sale_date DATE NOT NULL,
        total_amount REAL NOT NULL,
        FOREIGN KEY (product_id) REFERENCES products (product_id)
    )
    ''')

    conn.commit()
    conn.close()

# category functions
def add_category(name, description):
    conn = sqlite3.connect('inventory_management_v3.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO categories (category_name, description) VALUES (?, ?)', (name, description))
    conn.commit()
    conn.close()
    print(f"Category '{name}' added successfully.")

def view_categories():
    conn = sqlite3.connect('inventory_management_v3.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM categories')
    rows = cursor.fetchall()
    conn.close()

    if rows:
        for row in rows:
            print(f"ID: {row[0]}, Name: {row[1]}, Description: {row[2]}")
    else:
        print("No categories found.")

def update_category(category_id, name, description):
    conn = sqlite3.connect('inventory_management_v3.db')
    cursor = conn.cursor()
    cursor.execute('UPDATE categories SET category_name = ?, description = ? WHERE category_id = ?', (name, description, category_id))
    conn.commit()
    conn.close()
    print(f"Category ID {category_id} updated successfully.")

def delete_category(category_id):
    conn = sqlite3.connect('inventory_management_v3.db')
    cursor = conn.cursor()
    cursor.execute('DELETE FROM categories WHERE category_id = ?', (category_id,))
    conn.commit()
    conn.close()
    print(f"Category ID {category_id} deleted successfully.")

def category_management():
    while True:
        print("\n1. View Categories")
        print("2. Add Category")
        print("3. Update Category")
        print("4. Delete Category")
        print("5. Back to Main Menu")

        choice = input("Choose an option: ")

        if choice == '1':
            view_categories()
        elif choice == '2':
            name = input("Enter category name: ")
            description = input("Enter category description: ")
            add_category(name, description)
        elif choice == '3':
            category_id = int(input("Enter category ID to update: "))
            name = input("Enter new category name: ")
            description = input("Enter new description: ")
            update_category(category_id, name, description)
        elif choice == '4':
            category_id = int(input("Enter category ID to delete: "))
            delete_category(category_id)
        elif choice == '5':
            break
        else:
            print("Invalid option. Please try again.")

# supplier functions
def add_supplier(name, contact_info, address):
    conn = sqlite3.connect('inventory_management_v3.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO suppliers (supplier_name, contact_info, address) VALUES (?, ?, ?)', (name, contact_info, address))
    conn.commit()
    conn.close()
    print(f"Supplier '{name}' added successfully.")

def view_suppliers():
    conn = sqlite3.connect('inventory_management_v3.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM suppliers')
    rows = cursor.fetchall()
    conn.close()

    if rows:
        for row in rows:
            print(f"ID: {row[0]}, Name: {row[1]}, Contact: {row[2]}, Address: {row[3]}")
    else:
        print("No suppliers found.")

def update_supplier(supplier_id, name, contact_info, address):
    conn = sqlite3.connect('inventory_management_v3.db')
    cursor = conn.cursor()
    cursor.execute('UPDATE suppliers SET supplier_name = ?, contact_info = ?, address = ? WHERE supplier_id = ?', (name, contact_info, address, supplier_id))
    conn.commit()
    conn.close()
    print(f"Supplier ID {supplier_id} updated successfully.")

def delete_supplier(supplier_id):
    conn = sqlite3.connect('inventory_management_v3.db')
    cursor = conn.cursor()
    cursor.execute('DELETE FROM suppliers WHERE supplier_id = ?', (supplier_id,))
    conn.commit()
    conn.close()
    print(f"Supplier ID {supplier_id} deleted successfully.")

def supplier_management():
    while True:
        print("\n1. View Suppliers")
        print("2. Add Supplier")
        print("3. Update Supplier")
        print("4. Delete Supplier")
        print("5. Back to Main Menu")

        choice = input("Choose an option: ")

        if choice == '1':
            view_suppliers()
        elif choice == '2':
            name = input("Enter supplier name: ")
            contact_info = input("Enter contact info: ")
            address = input("Enter address: ")
            add_supplier(name, contact_info, address)
        elif choice == '3':
            supplier_id = int(input("Enter supplier ID to update: "))
            name = input("Enter new supplier name: ")
            contact_info = input("Enter new contact info: ")
            address = input("Enter new address: ")
            update_supplier(supplier_id, name, contact_info, address)
        elif choice == '4':
            supplier_id = int(input("Enter supplier ID to delete: "))
            delete_supplier(supplier_id)
        elif choice == '5':
            break
        else:
            print("Invalid option. Please try again.")
            
# product functions    
def add_product(name, category_id, supplier_id, stock_level, reorder_level, price):
    date_added = datetime.now().strftime('%Y-%m-%d')  # Current date
    conn = sqlite3.connect('inventory_management_v3.db')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO products (product_name, category_id, supplier_id, stock_level, reorder_level, price, date_added) 
        VALUES (?, ?, ?, ?, ?, ?, ?)
    ''', (name, category_id, supplier_id, stock_level, reorder_level, price, date_added))
    conn.commit()
    conn.close()
    print(f"Product '{name}' added successfully.")

def view_products():
    conn = sqlite3.connect('inventory_management_v3.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM products')
    rows = cursor.fetchall()
    conn.close()

    if rows:
        for row in rows:
            print(f"ID: {row[0]}, Name: {row[1]}, Stock Level: {row[4]}, Price: {row[6]}, Date Added: {row[7]}")
    else:
        print("No products found.")

def update_product(product_id, name, category_id, supplier_id, stock_level, reorder_level, price):
    conn = sqlite3.connect('inventory_management_v3.db')
    cursor = conn.cursor()
    cursor.execute('''
        UPDATE products SET product_name = ?, category_id = ?, supplier_id = ?, stock_level = ?, reorder_level = ?, price = ? 
        WHERE product_id = ?
    ''', (name, category_id, supplier_id, stock_level, reorder_level, price, product_id))
    conn.commit()
    conn.close()
    print(f"Product ID {product_id} updated successfully.")

def delete_product(product_id):
    conn = sqlite3.connect('inventory_management_v3.db')
    cursor = conn.cursor()
    cursor.execute('DELETE FROM products WHERE product_id = ?', (product_id,))
    conn.commit()
    conn.close()
    print(f"Product ID {product_id} deleted successfully.")

def product_management():
    while True:
        print("\n1. View Products")
        print("2. Add Product")
        print("3. Update Product")
        print("4. Delete Product")
        print("5. Back to Main Menu")

        choice = input("Choose an option: ")

        if choice == '1':
            view_products()
        elif choice == '2':
            name = input("Enter product name: ")
            category_id = int(input("Enter category ID: "))
            supplier_id = int(input("Enter supplier ID: "))
            stock_level = int(input("Enter stock level: "))
            reorder_level = int(input("Enter reorder level: "))
            price = float(input("Enter price: "))
            add_product(name, category_id, supplier_id, stock_level, reorder_level, price)
        elif choice == '3':
            product_id = int(input("Enter product ID to update: "))
            name = input("Enter new product name: ")
            category_id = int(input("Enter new category ID: "))
            supplier_id = int(input("Enter new supplier ID: "))
            stock_level = int(input("Enter new stock level: "))
            reorder_level = int(input("Enter new reorder level: "))
            price = float(input("Enter new price: "))
            update_product(product_id, name, category_id, supplier_id, stock_level, reorder_level, price)
        elif choice == '4':
            product_id = int(input("Enter product ID to delete: "))
            delete_product(product_id)
        elif choice == '5':
            break
        else:
            print("Invalid option. Please try again.")

# # sales function            
def add_sale(product_id, quantity_sold, sale_date, total_amount):
    conn = sqlite3.connect('inventory_management_v3.db')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO sales (product_id, quantity_sold, sale_date, total_amount) 
        VALUES (?, ?, ?, ?)
    ''', (product_id, quantity_sold, sale_date, total_amount))
    conn.commit()
    conn.close()
    print(f"Sale recorded for product ID {product_id}.")

def record_sale(product_id, quantity_sold, total_amount):
    conn = sqlite3.connect('inventory_management_v3.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO sales (product_id, quantity_sold, sale_date, total_amount) VALUES (?, ?, ?, ?)', 
                   (product_id, quantity_sold, datetime.now(), total_amount))
    conn.commit()
    conn.close()
    print(f"Sale recorded for Product ID {product_id}.")

def view_sales():
    conn = sqlite3.connect('inventory_management_v3.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM sales')
    rows = cursor.fetchall()
    conn.close()

    if rows:
        for row in rows:
            print(f"Sale ID: {row[0]}, Product ID: {row[1]}, Quantity Sold: {row[2]}, Date: {row[3]}, Total Amount: {row[4]}")
    else:
        print("No sales recorded.")

def sale_management():
    while True:
        print("\n1. View Sales")
        print("2. Record Sale")
        print("3. Back to Main Menu")

        choice = input("Choose an option: ")

        if choice == '1':
            view_sales()
        elif choice == '2':
            product_id = int(input("Enter product ID: "))
            quantity_sold = int(input("Enter quantity sold: "))
            total_amount = float(input("Enter total amount: "))
            record_sale(product_id, quantity_sold, total_amount)
        elif choice == '3':
            break
        else:
            print("Invalid option. Please try again.")


def main():
    create_tables()

    # Sample data
    add_category('Electronics', 'Devices and gadgets')
    add_category('Clothing', 'Apparel and accessories')
    add_category('Home Goods', 'Household items')
    add_category('Groceries', 'Food and beverages')

    add_supplier('Tech Supplier', 'tech@example.com', '123 Tech St, City A')
    add_supplier('Fashion Corp', 'fashion@example.com', '456 Fashion Rd, City B')
    add_supplier('Home Goods Inc', 'homegoods@example.com', '789 Home Ave, City C')
    add_supplier('Food Suppliers', 'food@example.com', '321 Food Ln, City D')

    add_product('Smartphone', 1, 1, 50, 10, 699.99)
    add_product('T-shirt', 2, 2, 200, 50, 19.99)
    add_product('Blender', 3, 3, 30, 15, 49.99)
    add_product('Coffee Maker', 3, 3, 15, 5, 89.99)
    add_product('Pasta', 4, 4, 100, 20, 2.99)
    add_product('Jeans', 2, 2, 80, 20, 39.99)
    add_product('Wireless Headphones', 1, 1, 25, 5, 149.99)
    add_product('Olive Oil', 4, 4, 60, 15, 8.99)

    add_sale(1, 5, '2024-01-15', 3499.95)
    add_sale(2, 10, '2024-01-17', 199.90)
    add_sale(3, 2, '2024-01-18', 99.98)
    add_sale(4, 1, '2024-01-20', 89.99)
    add_sale(5, 20, '2024-01-21', 59.80)
    add_sale(6, 4, '2024-01-22', 159.96)
    add_sale(7, 3, '2024-01-23', 449.97)
    add_sale(8, 15, '2024-01-24', 134.85)

    while True:
        print("\n1. Manage Categories")
        print("2. Manage Suppliers")
        print("3. Manage Products")
        print("4. Record Sale")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            category_management()
        elif choice == '2':
            supplier_management()
        elif choice == '3':
            product_management()
        elif choice == '4':
            sale_management()
        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()