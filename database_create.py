import sqlite3

def create_database():
    conn = sqlite3.connect('cooksoo_cafe.db')
    cur = conn.cursor()


    cur.execute('''CREATE TABLE IF NOT EXISTS user (
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   name TEXT NOT NULL,
                   phone TEXT NOT NULL,
                   role TEXT CHECK(role IN ('kitchen', 'administration', 'courier', 'user')) NOT NULL
                   )''')


    cur.execute('''CREATE TABLE IF NOT EXISTS categories (
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   name TEXT NOT NULL
                   )''')

    cur.execute('''CREATE TABLE IF NOT EXISTS dishes (
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   name TEXT NOT NULL,
                   price REAL NOT NULL,
                   category_id INTEGER,
                   sub_category_id INTEGER, 
                   img_link TEXT,
                   FOREIGN KEY (category_id) REFERENCES categories (id),
                   FOREIGN KEY (sub_category_id) REFERENCES sub_category (id)
                   )''')

    cur.execute('''CREATE TABLE IF NOT EXISTS promocodes (
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   code TEXT NOT NULL,
                   discount REAL NOT NULL,
                   qr_code BLOB
                   )''')

    cur.execute('''CREATE TABLE IF NOT EXISTS orders (
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   description TEXT,
                   status TEXT,
                   user_id INTEGER,
                   dish_id INTEGER,
                   FOREIGN KEY (user_id) REFERENCES user (id),
                   FOREIGN KEY (dish_id) REFERENCES dishes (id)
                   )''')

    cur.execute('''CREATE TABLE IF NOT EXISTS branch (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    address TEXT NOT NULL,
                    phone TEXT NOT NULL
                     )''')

    cur.execute('''CREATE TABLE IF NOT EXISTS sub_category (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    category_id INTEGER,
                    FOREIGN KEY (category_id) REFERENCES categories (id)
                    )''')
                    

    cur.execute('''INSERT INTO categories (name) VALUES ('Beverages');''')
    cur.execute('''INSERT INTO categories (name) VALUES ('Main Dishes');''')
    cur.execute('''INSERT INTO categories (name) VALUES ('Desserts');''')  
                    
    cur.execute('''INSERT INTO sub_category (name, category_id) VALUES ('Coffee', 1);''')
    cur.execute('''INSERT INTO sub_category (name, category_id) VALUES ('Tea', 1);''')
    cur.execute('''INSERT INTO sub_category (name, category_id) VALUES ('Soft Drinks', 1);''')
    cur.execute('''INSERT INTO sub_category (name, category_id) VALUES ('Pasta', 2);''')
    cur.execute('''INSERT INTO sub_category (name, category_id) VALUES ('Burgers', 2);''')
    cur.execute('''INSERT INTO sub_category (name, category_id) VALUES ('Salads', 2);''')
    cur.execute('''INSERT INTO sub_category (name, category_id) VALUES ('Cakes', 3);''')
    cur.execute('''INSERT INTO sub_category (name, category_id) VALUES ('Ice Cream', 3);''')

        
    cur.execute('''INSERT INTO dishes (name, price, category_id, sub_category_id, img_link) VALUES ('Green Tea', 2.50, 1, 2, 'https://hips.hearstapps.com/hmg-prod/images/green-tea-wight-loss-1643990040.jpg?crop=0.665xw:1.00xh;0.291xw,0&resize=1200:*');''')
    cur.execute('''INSERT INTO dishes (name, price, category_id, sub_category_id, img_link) VALUES ('Black Tea', 2.50, 1, 2, 'https://clubmagichour.com/cdn/shop/articles/AdobeStock_316822193.jpg?v=1688754552');''')


    cur.execute('''INSERT INTO dishes (name, price, category_id, sub_category_id, img_link) VALUES ('Cola', 1.99, 1, 3, 'https://arigato.kg/wp-content/uploads/2022/12/cola-600x600-1.png');''')
    cur.execute('''INSERT INTO dishes (name, price, category_id, sub_category_id, img_link) VALUES ('Fanta', 1.99, 1, 3, 'https://www.coca-cola.co.uk/content/dam/one/gb/en/heritage/brands/brand-fanta-uk-1.png');''')
    cur.execute('''INSERT INTO dishes (name, price, category_id, sub_category_id, img_link) VALUES ('Sprite', 1.99, 1, 3, 'https://www.coca-cola.co.uk/content/dam/one/gb/en/heritage/brands/brand-sprite-uk-1.png');''')
    cur.execute('''INSERT INTO dishes (name, price, category_id, sub_category_id, img_link) VALUES ('Lemonade', 2.50, 1, 3, 'https://www.foodiecrush.com/wp-content/uploads/2022/06/Lemonade-foodiecrush.com-9-1.jpg');''')

    cur.execute("INSERT INTO dishes (name, price, category_id, sub_category_id, img_link) VALUES ('Spaghetti Carbonara', 8.99, 2, 4, 'https://images.services.kitchenstories.io/6glN_4JhpVS9aUiBS7JnGsuDULA=/3840x0/filters:quality(80)/images.kitchenstories.io/wagtailOriginalImages/R2568-photo-final-_0.jpg');")
    cur.execute("INSERT INTO dishes (name, price, category_id, sub_category_id, img_link) VALUES ('Penne Arrabbiata', 7.99, 2, 4, 'https://theplantbasedschool.com/wp-content/uploads/2022/04/Arrabbiata-in-pan-1.jpg');")

    cur.execute("INSERT INTO dishes (name, price, category_id, sub_category_id, img_link) VALUES ('Classic Beef Burger', 6.99, 2, 5, 'https://realfood.tesco.com/media/images/Burger-31LGH-a296a356-020c-4969-86e8-d8c26139f83f-0-1400x919.jpg');")
    cur.execute("INSERT INTO dishes (name, price, category_id, sub_category_id, img_link) VALUES ('Veggie Burger', 5.99, 2, 5, 'https://www.realsimple.com/thmb/z3cQCYXTyDQS9ddsqqlTVE8fnpc=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc()/real-simple-mushroom-black-bean-burgers-recipe-0c365277d4294e6db2daa3353d6ff605.jpg');")

    cur.execute("INSERT INTO dishes (name, price, category_id, sub_category_id, img_link) VALUES ('Caesar Salad', 5.99, 2, 6, 'https://www.seriouseats.com/thmb/Fi_FEyVa3_-_uzfXh6OdLrzal2M=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc()/the-best-caesar-salad-recipe-06-40e70f549ba2489db09355abd62f79a9.jpg');")
    cur.execute("INSERT INTO dishes (name, price, category_id, sub_category_id, img_link) VALUES ('Greek Salad', 4.99, 2, 6, 'https://www.thehungrybites.com/wp-content/uploads/2017/07/Authentic-Greek-salad-horiatiki-featured.jpg');")

    cur.execute("INSERT INTO dishes (name, price, category_id, sub_category_id, img_link) VALUES ('Cheesecake', 3.99, 3, 7, 'https://joyfoodsunshine.com/wp-content/uploads/2022/03/best-cheesecake-recipe-6.jpg');")
    cur.execute("INSERT INTO dishes (name, price, category_id, sub_category_id, img_link) VALUES ('Chocolate Cake', 3.99, 3, 7, 'https://hips.hearstapps.com/hmg-prod/images/chocolate-cake-index-64b83bce2df26.jpg?crop=0.6668359143606668xw:1xh;center,top&resize=1200:*');")

    cur.execute("INSERT INTO dishes (name, price, category_id, sub_category_id, img_link) VALUES ('Vanilla Ice Cream', 2.99, 3, 8, 'https://www.washingtonpost.com/wp-apps/imrs.php?src=https://arc-anglerfish-washpost-prod-washpost.s3.amazonaws.com/public/KUFWIPXROII6ZLAWR67XDFGNPA.jpg&w=1440');")
    cur.execute("INSERT INTO dishes (name, price, category_id, sub_category_id, img_link) VALUES ('Strawberry Ice Cream', 2.99, 3, 8, 'https://www.thespruceeats.com/thmb/kpuMkqk0BhGMTuSENf_IebbHu1s=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc()/strawberry-ice-cream-10-0b3e120e7d6f4df1be3c57c17699eb2c.jpg');")

    conn.commit()
    conn.close()

if __name__ == '__main__':
    create_database()