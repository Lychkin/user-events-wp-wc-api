# Скрипт который будет загружать данные из CSV в БД sqlite events.db
# Удобно, когда нужно быстро наполнить базу данных

import csv
from datetime import datetime
from pathlib import Path

from models.event import UserEvent
from database import engine, Base, SessionLocal

# создаём таблицу если её нет
Base.metadata.create_all(bind=engine)


def import_csv_to_db(csv_file_path: str, batch_size: int = 1000):
    session = SessionLocal()

    inserted = 0
    batch = []

    try:
        with open(csv_file_path, "r", encoding="utf-8") as file:
            reader = csv.DictReader(file)

            for row in reader:
                # валидация event
                if row["event"] not in ("view", "add_to_cart"):
                    print(f"Skip invalid event: {row}")
                    continue

                batch.append(
                    {
                        "item_id": int(row["item_id"]),
                        "user_id": int(row["user_id"]),
                        "timestamp": datetime.fromisoformat(row["timestamp"]),
                        "event": row["event"],
                    }
                )

                # массовая вставка
                if len(batch) >= batch_size:
                    session.bulk_insert_mappings(UserEvent, batch)
                    session.commit()

                    inserted += len(batch)
                    print(f"Inserted: {inserted}")

                    batch.clear()

            # вставляем остаток
            if batch:
                session.bulk_insert_mappings(UserEvent, batch)
                session.commit()

                inserted += len(batch)

        print(f"\nImport completed. Total inserted: {inserted}")

    except Exception as e:
        session.rollback()
        print("ERROR:", e)

    finally:
        session.close()


if __name__ == "__main__":
    csv_file = (
        Path(__file__).resolve().parent.parent / "data" / "add-events.csv"
    )
    import_csv_to_db(csv_file)
