from fastapi import APIRouter
import psycopg2
from psycopg2 import Error

# Khởi tạo router
router = APIRouter()

# Thông tin kết nối đến cơ sở dữ liệu PostgreSQL
connection_info = {
    "host": "ep-late-violet-a256iomj.eu-central-1.pg.koyeb.app",
    "database": "bisu",
    "user": "koyeb-adm",
    "password": "KeyN2Cq1oUjl",
}


# Định nghĩa tuyến API để lấy danh sách người dùng
@router.get("/users")
def get_users():
    try:
        # Kết nối đến cơ sở dữ liệu
        connection = psycopg2.connect(**connection_info)

        # Tạo một đối tượng cursor để thực thi các truy vấn SQL
        cursor = connection.cursor()

        # Truy vấn SQL để lấy danh sách người dùng
        select_query = """
        SELECT * FROM users;
        """

        # Thực thi truy vấn SQL
        cursor.execute(select_query)

        # Lấy tất cả các dòng kết quả
        users = cursor.fetchall()

        data_array = [
            {"id": user[0], "name": user[1], "email": user[2]} for user in users
        ]

        return data_array

    except Error as e:
        return {"error": f"Lỗi khi lấy danh sách người dùng: {e}"}

    finally:
        # Đóng kết nối và cursor
        if connection:
            cursor.close()
            connection.close()
