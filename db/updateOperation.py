import sqlite3

def updateUserAccess(id,approved,blocked):
    conn=sqlite3.connect("my_medicalShop.db")
    cursor=conn.cursor()
    cursor.execute("""UPDATE User SET approved=?, Block=? WHERE id= ? """, (approved,blocked, id))
    conn.commit()
    conn.close()
    return True