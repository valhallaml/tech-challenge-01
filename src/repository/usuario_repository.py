from sqlalchemy.orm import Session
from model.usuario import Usuario


class UsuarioRepository:
    @staticmethod
    def find_all(db: Session) -> list[Usuario]:
        return db.query(Usuario).all()

    @staticmethod
    def save(db: Session, usuario: Usuario) -> Usuario:
        if usuario.id:
            db.merge(usuario)
        else:
            db.add(usuario)
        db.commit()
        return usuario

    @staticmethod
    def find_by_id(db: Session, id: int) -> Usuario:
        return db.query(Usuario).filter(Usuario.id == id).first()

    @staticmethod
    def find_by_username(db: Session, username: str) -> Usuario:
        return db.query(Usuario).filter(Usuario.username == username).first()

    @staticmethod
    def exists_by_id(db: Session, id: int) -> bool:
        return db.query(Usuario).filter(Usuario.id == id).first() is not None

    @staticmethod
    def delete_by_id(db: Session, id: int) -> None:
        curso = db.query(Usuario).filter(Usuario.id == id).first()
        if curso is not None:
            db.delete(curso)
            db.commit()