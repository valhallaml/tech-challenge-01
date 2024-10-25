from sqlalchemy.orm import Session
from model.user import User


class UserRepository:
    @staticmethod
    def find_all(db: Session) -> list[User]:
        return db.query(User).all()

    @staticmethod
    def save(db: Session, User: User) -> User:
        if User.id:
            db.merge(User)
        else:
            db.add(User)
        db.commit()
        return User

    @staticmethod
    def find_by_id(db: Session, id: int) -> User:
        return db.query(User).filter(User.id == id).first()

    @staticmethod
    def find_by_username(db: Session, username: str) -> User:
        return db.query(User).filter(User.username == username).first()

    @staticmethod
    def find_by_mail(db: Session, mail: str) -> User:
        return db.query(User).filter(User.mail == mail).first()

    @staticmethod
    def exists_by_id(db: Session, id: int) -> bool:
        return db.query(User).filter(User.id == id).first() is not None

    @staticmethod
    def delete_by_id(db: Session, id: int) -> None:
        curso = db.query(User).filter(User.id == id).first()
        if curso is not None:
            db.delete(curso)
            db.commit()