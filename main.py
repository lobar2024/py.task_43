class DatabaseConnection:
    def __init__(self, db_name):
        self.db_name = db_name
        self.connection = None
        self.queries = []

    def __enter__(self):
        print(f"[DB] {self.db_name} ga ulanildi")
        self.connection = True
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is None:
            self._commit()
        else:
            self._rollback()
            print(f"[DB] Xato: {exc_val}")
        self.connection = None
        print(f"[DB] Ulanish yopildi")
        return True  # xatoni "yutadi"

    def execute(self, query):
        if not self.connection:
            raise RuntimeError("Ulanish yo'q")
        self.queries.append(query)
        print(f"[DB] Bajarildi: {query}")

    def _commit(self):
        print(f"[DB] COMMIT — {len(self.queries)} ta query saqlandi")

    def _rollback(self):
        print(f"[DB] ROLLBACK — {len(self.queries)} ta query bekor qilindi")

# Muvaffaqiyatli holat
with DatabaseConnection("users_db") as db:
    db.execute("INSERT INTO users VALUES ('Ali', 25)")
    db.execute("UPDATE users SET age=26 WHERE name='Ali'")

print()

# Xatoli holat
with DatabaseConnection("orders_db") as db:
    db.execute("INSERT INTO orders VALUES (1, 'Laptop')")
    raise ValueError("To'lov amalga oshmadi!")
    db.execute("UPDATE stock SET qty=qty-1")
