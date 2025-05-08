from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.session import SessionLocal
from app.models.project import Project
from app.schemas.schemas import ProjectCreate, ProjectResponse, ProjectUpdate

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/projects", response_model=list[ProjectResponse])
def list_projects(db: Session = Depends(get_db)):
    return db.query(Project).all()

@router.get("/projects/{project_id}", response_model=ProjectResponse)
def get_project(project_id: int, db: Session = Depends(get_db)):
    project = db.query(Project).get(project_id)
    if not project:
        raise HTTPException(status_code=404, detail="Projeto não encontrado")
    return project

@router.post("/projects", response_model=ProjectResponse)
def create_project(project: ProjectCreate, db: Session = Depends(get_db)):
    db_project = Project(**project.model_dump())
    db.add(db_project)
    db.commit()
    db.refresh(db_project)
    return db_project


@router.get("/projects-status")
def count_project_status(db: Session = Depends(get_db)):
    ativos = db.query(Project).filter_by(status="Ativo").count()
    pausados = db.query(Project).filter_by(status="Pausado").count()
    finalizados = db.query(Project).filter_by(status="Finalizado").count()

    return {
        "Ativo": ativos,
        "Pausado": pausados,
        "Finalizado": finalizados
    }

@router.put("/projects/{project_id}", response_model=ProjectResponse)
def update_project(project_id: int, update: ProjectUpdate, db: Session = Depends(get_db)):
    project = db.query(Project).get(project_id)
    if not project:
        raise HTTPException(status_code=404, detail="Projeto não encontrado")
    for key, value in update.dict().items():
        setattr(project, key, value)
    db.commit()
    db.refresh(project)
    return project

@router.delete("/projects/{project_id}")
def delete_project(project_id: int, db: Session = Depends(get_db)):
    project = db.query(Project).get(project_id)
    if not project:
        raise HTTPException(status_code=404, detail="Projeto não encontrado")
    db.delete(project)
    db.commit()
    return {"ok": True}
