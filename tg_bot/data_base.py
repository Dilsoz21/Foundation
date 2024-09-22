import psycopg2

data_base = psycopg2.connect(
    host='tai.db.elephantsql.com',
    user='lsaoqoqn',
    database='lsaoqoqn',
    password='7PTZcca9ldtpzTYD5a80sNSIny8Huaog'
)

cursor = data_base.cursor()

def insert_data(laptop_name, laptop_image, laptop_price, credit_price):
    cursor.execute(f"""
        INSERT INTO laptops(laptop_name, laptop_image, laptop_price, credit_price)
        VALUES
        ('{laptop_name}', '{laptop_image}', '{laptop_price}', '{credit_price}')
    """)

    data_base.commit()


cursor.execute("""
    SELECT laptop_name, laptop_image, laptop_price, credit_price
    FROM laptops
""")


data = cursor.fetchall()

print(data)



