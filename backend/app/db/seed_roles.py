
from sqlalchemy import select

from app.db.session import SessionLocal
from app.models.role import Role


DEFAULT_ROLES = [
    {
        "name": "Admin",
        "description": "Manages the entire WorkSphere platform",
    },
    {
        "name": "Project Manager",
        "description": "Manages projects, teams and tasks",
    },
    {
        "name": "Developer",
        "description": "Works on assigned development tasks",
    },
    {
        "name": "Tester",
        "description": "Tests features and reports bugs",
    },
]


def seed_roles():
    db = SessionLocal()

    try:
        for role_data in DEFAULT_ROLES:
            existing_role = db.scalar(
                select(Role).where(
                    Role.name == role_data["name"]
                )
            )

            if existing_role is None:
                db.add(Role(**role_data))
                print(f"Created role: {role_data['name']}")
            else:
                print(f"Role already exists: {role_data['name']}")

        db.commit()
        print("Role seeding completed successfully.")

    except Exception:
        db.rollback()
        raise

    finally:
        db.close()


if __name__ == "__main__":
    seed_roles()
