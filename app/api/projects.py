from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.session import SessionLocal
from app.models.project import Project
from app.schemas.schemas import ProjectCreate, ProjectResponse, ProjectUpdate

router = APIRouter()

async def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/", response_model=list[ProjectResponse])
async def list_projects(db: Session = Depends(get_db)):
    return db.query(Project).all()

@router.get("/projects-status")
async def count_project_status(db: Session = Depends(get_db)):
    ativos = db.query(Project).filter_by(status="Ativo").count()
    pausados = db.query(Project).filter_by(status="Pausado").count()
    finalizados = db.query(Project).filter_by(status="Finalizado").count()

    return {
        "Ativo": ativos,
        "Pausado": pausados,
        "Finalizado": finalizados
    }

@router.get("/{project_id}", response_model=ProjectResponse)
async def get_project(project_id: int, db: Session = Depends(get_db)):
    project = db.get(Project, project_id)
    if not project:
        raise HTTPException(status_code=404, detail="Projeto não encontrado")
    return project

@router.post("/", response_model=ProjectResponse)
async def create_project(project: ProjectCreate, db: Session = Depends(get_db)):
    db_project = Project(**project.model_dump())
    db.add(db_project)
    db.commit()
    db.refresh(db_project)
    return db_project

@router.put("/{project_id}", response_model=ProjectResponse)
async def update_project(project_id: int, update: ProjectUpdate, db: Session = Depends(get_db)):
    project = db.get(Project, project_id)
    if not project:
        raise HTTPException(status_code=404, detail="Projeto não encontrado")
    for key, value in update.model_dump().items():
        setattr(project, key, value)
    db.commit()
    db.refresh(project)
    return project

@router.delete("/{project_id}")
async def delete_project(project_id: int, db: Session = Depends(get_db)):
    project = db.get(Project, project_id)
    if not project:
        raise HTTPException(status_code=404, detail="Projeto não encontrado")
    db.delete(project)
    db.commit()
    return {"ok": True}
