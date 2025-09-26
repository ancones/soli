from sqlalchemy.orm import Session
from model.solicitud import Solicitud
from sqlalchemy import text

class SolicitudRepository:
    def create_solicitud(self, db: Session, solicitud_data):
        db_solicitud = Solicitud(**solicitud_data)
        db.add(db_solicitud)
        db.commit()
        db.refresh(db_solicitud)
        return db_solicitud

    def get_solicitudes(self, db: Session):
        return db.query(Solicitud).all()

    def get_solicitudes_by_user_id(self, db: Session, user_id: str):
        query = text("""
            SELECT 
                s.id_solicitud AS "ID", 
                a.nombre AS "Area", 
                t_s.nombre AS "Tipo", 
                e.nombre AS "Estado", 
                s.descripcion AS "Description"
            FROM solicitud s
            JOIN area a ON a.id_area = s.id_area
            JOIN tipo_solicitud t_s ON t_s.id_tipo_solicitud = s.id_tipo_solicitud
            JOIN estado_solicitud e ON e.id_estado = s.id_estado
            WHERE s.user_id = :user_id
        """)
        return db.execute(query, {"user_id": user_id}).mappings().all()

    def get_format_solicitudes(self, db: Session):
        query = text("""
            SELECT 
                s.id_solicitud AS "ID", 
                a.nombre AS "Area", 
                t_s.nombre AS "Tipo", 
                e.nombre AS "Estado", 
                s.descripcion AS "Description"
            FROM solicitud s
            JOIN area a ON a.id_area = s.id_area
            JOIN tipo_solicitud t_s ON t_s.id_tipo_solicitud = s.id_tipo_solicitud
            JOIN estado_solicitud e ON e.id_estado = s.id_estado
        """)
        return db.execute(query).mappings().all()